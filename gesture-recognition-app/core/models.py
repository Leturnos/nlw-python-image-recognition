from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import joblib


@dataclass(frozen=True)
class ModelPaths:
    mp_task: Path
    custom_model: Path
    label_encoder: Path


@dataclass(frozen=True)
class CustomGestureArtifacts:
    clf: object
    label_encoder: object


def default_model_paths() -> ModelPaths:
    core_dir = Path(__file__).resolve().parent
    models_dir = (core_dir / ".." / "models").resolve()

    return ModelPaths(
        mp_task=models_dir / "gesture_recognizer.task",
        custom_model=models_dir / "gesture_model.joblib",
        label_encoder=models_dir / "label_encoder.joblib",
    )


def validate_model_files(*paths: Path) -> list[Path]:
    return [p for p in paths if not p.exists()]


def load_custom_gesture_artifacts(*, model_path: Path, encoder_path: Path) -> CustomGestureArtifacts:
    clf = joblib.load(model_path)
    label_encoder = joblib.load(encoder_path)
    return CustomGestureArtifacts(clf=clf, label_encoder=label_encoder)

