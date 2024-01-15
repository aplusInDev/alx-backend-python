#!/usr/bin/env python3
"""This module contains the function for task 4"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of delays in ascending order"""
    delays: List[float] = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))
    return sorted([await delay for delay in delays])
