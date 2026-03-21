from __future__ import annotations

import atexit
import base64
import logging
import time
from pathlib import Path

import cv2
import mediapipe as mp
import numpy as np

from core.models import default_model_paths, load_custom_gesture_artifacts, validate_model_files

# Suppress INFO logs from MediaPipe and TensorFlow
logging.getLogger("absl").setLevel(logging.ERROR)


def create_gesture_recognizer(*, model_asset_path: str):
    BaseOptions = mp.tasks.BaseOptions
    GestureRecognizer = mp.tasks.vision.GestureRecognizer
    GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
    VisionRunningMode = mp.tasks.vision.RunningMode

    options = GestureRecognizerOptions(
        base_options=BaseOptions(model_asset_path=model_asset_path),
        running_mode=VisionRunningMode.VIDEO,
        num_hands=2,
        min_hand_detection_confidence=0.5,
        min_hand_presence_confidence=0.5,
        min_tracking_confidence=0.5,
    )
    return GestureRecognizer.create_from_options(options)


def _landmarks_to_features(hand_landmarks, *, handedness_label: str) -> np.ndarray:
    handedness_val = 0 if handedness_label == "Left" else 1
    landmarks_array: list[float] = [float(handedness_val)]
    for lm in hand_landmarks:
        landmarks_array.extend([float(lm.x), float(lm.y), float(lm.z)])
    return np.asarray(landmarks_array, dtype=np.float32).reshape(1, -1)


class GestureProcessor:
    def __init__(self):
        paths = default_model_paths()
        missing = validate_model_files(paths.mp_task, paths.custom_model, paths.label_encoder)
        if missing:
            missing_str = "\n".join(f"- {p}" for p in missing)
            raise FileNotFoundError("Os seguintes arquivos de modelo não foram encontrados:\n" + missing_str)

        artifacts = load_custom_gesture_artifacts(
            model_path=paths.custom_model, encoder_path=paths.label_encoder
        )
        self.clf = artifacts.clf
        self.label_encoder = artifacts.label_encoder

        self.recognizer = create_gesture_recognizer(model_asset_path=str(paths.mp_task))
        atexit.register(self.recognizer.close)

        self.gesture_images = self._load_gesture_images()

    def _load_gesture_images(self):
        img_dir = Path(__file__).resolve().parent.parent / "assets" / "img"
        gesture_images = {}
        for img_path in img_dir.glob("*.png"):
            try:
                # Use filename (without extension) as gesture name
                gesture_name = img_path.stem.lower()
                with open(img_path, "rb") as f:
                    # Encode image to base64 string
                    encoded_string = base64.b64encode(f.read()).decode("utf-8")
                    gesture_images[gesture_name] = f"data:image/png;base64,{encoded_string}"
            except Exception as e:
                print(f"Error loading gesture image {img_path}: {e}")
        return gesture_images

    def process_frame(self, frame_bgr: np.ndarray, draw_landmarks: bool):
        if frame_bgr is None:
            raise ValueError("frame_bgr cannot be None")

        frame = frame_bgr.copy()
        frame = cv2.flip(frame, 1)  # Mirror frame

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        timestamp_ms = int(time.time() * 1000)

        recognition_result = self.recognizer.recognize_for_video(mp_image, timestamp_ms)

        labels = []
        gesture_img_b64 = None

        if recognition_result.hand_landmarks:
            for i, hand_landmarks in enumerate(recognition_result.hand_landmarks):
                if draw_landmarks:
                    mp_drawing = mp.tasks.vision.drawing_utils
                    mp_drawing_styles = mp.tasks.vision.drawing_styles
                    mp_hands = mp.tasks.vision.HandLandmarksConnections
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style(),
                    )

                handedness = recognition_result.handedness[i][0]
                features = _landmarks_to_features(hand_landmarks, handedness_label=handedness.category_name)

                prediction_idx = self.clf.predict(features)[0]
                prediction_prob = float(np.max(self.clf.predict_proba(features)))
                gesture_name = self.label_encoder.inverse_transform([prediction_idx])[0]

                # Swap handedness for display on mirrored image
                display_hand = "Right hand" if handedness.category_name == "Left" else "Left hand"

                labels.append(
                    {
                        "hand": display_hand,
                        "gesture": gesture_name,
                        "prob": round(prediction_prob * 100, 2),
                    }
                )

                # Get gesture image if probability is high
                if prediction_prob > 0.7:
                    gesture_img_b64 = self.gesture_images.get(gesture_name.lower())

                # # Draw label on the frame
                # cv2.putText(
                #     frame,
                #     f"{display_hand}: {gesture_name} ({prediction_prob:.2f})",
                #     (20, 50 + (i * 40)),
                #     cv2.FONT_HERSHEY_SIMPLEX,
                #     0.8,
                #     (0, 255, 0),
                #     2,
                # )

        return frame, labels, gesture_img_b64
