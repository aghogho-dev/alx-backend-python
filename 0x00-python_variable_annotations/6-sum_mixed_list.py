#!/usr/bin/env python3
"""Mixed list with int and float."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Args:
      mxd_list(list(int | float)
    Return: sum as float
    """
    return sum(mxd_lst)
