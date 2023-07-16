#!/usr/bin/env python3
"""Async generator."""
import asyncio
from random import random
from typing import Generator



async def async_generator() -> Generator[float, None, None]:
    """Asyn generator func"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random() * 10
