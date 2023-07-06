#!/usr/bin/env python3
"""Complex function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
      multiplier(float)
    Returns a function
    """
    def multiply(n: float) -> float:
        """
        Args:
          n(float) - multiply with
        Return product of multipleir, n
        """
        return float(n * multiplier)
    return multiply
