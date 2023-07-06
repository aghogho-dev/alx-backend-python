#!/usr/bin/env python3
"""Mixed types and tuple."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
      k(str)
      v: int | float
    Return tuple(str | float)
    """
    return k, v**2
