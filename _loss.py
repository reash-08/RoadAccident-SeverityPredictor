import importlib

_sklearn_loss = importlib.import_module("sklearn._loss")

from sklearn._loss import link, loss
from sklearn._loss._loss import (
    __pyx_unpickle_CyHalfMultinomialLoss,
    CyHalfMultinomialLoss,
    CyHalfSquaredError,
    CyHalfGammaLoss,
    CyHalfTweedieLoss,
    CyHalfTweedieLossIdentity,
    CyHalfPoissonLoss,
    CyHalfBinomialLoss,
    CyHuberLoss,
    CyPinballLoss,
    CyExponentialLoss,
    CyAbsoluteError,
    CyLossFunction,
)

__all__ = [
    "link",
    "loss",
    "__pyx_unpickle_CyHalfMultinomialLoss",
    "CyHalfMultinomialLoss",
    "CyHalfSquaredError",
    "CyHalfGammaLoss",
    "CyHalfTweedieLoss",
    "CyHalfTweedieLossIdentity",
    "CyHalfPoissonLoss",
    "CyHalfBinomialLoss",
    "CyHuberLoss",
    "CyPinballLoss",
    "CyExponentialLoss",
    "CyAbsoluteError",
    "CyLossFunction",
]


def __getattr__(name):
    return getattr(_sklearn_loss, name)
