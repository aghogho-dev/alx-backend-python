#!/usr/bin/env python3
"""Multiple coroutines."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
      n(int): number of times.
      max_delay(int): max delay.
    Returns: list of wait time.
    """
    worker = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await work for work in asyncio.as_completed(worker)]
