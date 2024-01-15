#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """Measures the total execution time for wait_n"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
