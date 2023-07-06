#!/usr/bin/env python3
"""Iterable object type."""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Iterable object type."""
    return [(k, len(k)) for k in lst]
