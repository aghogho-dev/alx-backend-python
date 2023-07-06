#!/usr/bin/env python3
"""Any type."""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Any type."""
    if lst:
        return lst[0]
    return None
