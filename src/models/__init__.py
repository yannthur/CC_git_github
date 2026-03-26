"""Model architectures."""

import torch
import torch.nn as nn


class SimpleModel(nn.Module):
    """Simple neural network model."""

    def __init__(self) -> None:
        super().__init__()
        self.fc = nn.Linear(10, 2)

    def forward(self, x: torch.Tensor) -> torch.Tensor:  # type: ignore[name-defined]
        return self.fc(x)


def build_model() -> SimpleModel:
    """Build and return the model."""
    return SimpleModel()
