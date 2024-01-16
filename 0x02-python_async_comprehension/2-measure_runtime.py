#!/usr/bin/env python3
""" Async Comprehensions """

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Async Comprehensions """
    start = time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time() - start
