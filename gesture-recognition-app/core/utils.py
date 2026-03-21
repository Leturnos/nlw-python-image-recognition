import base64

import cv2
import numpy as np


def decode_image(jpg_b64: str) -> np.ndarray:
    """Decodes a base64-encoded JPEG string into an OpenCV image."""
    buf = base64.b64decode(jpg_b64)
    arr = np.frombuffer(buf, dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Falha ao decodificar JPEG")
    return img


def encode_image(img_bgr: np.ndarray, *, quality: int = 80) -> str:
    """Encodes an OpenCV image into a base64-encoded JPEG string."""
    ok, encoded = cv2.imencode(".jpg", img_bgr, [int(cv2.IMWRITE_JPEG_QUALITY), int(quality)])
    if not ok:
        raise ValueError("Falha ao codificar JPEG")
    return base64.b64encode(encoded.tobytes()).decode("ascii")
