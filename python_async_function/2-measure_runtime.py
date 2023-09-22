#!/usr/bin/env python3
'''
Module that measures the total execution time for wait_n(n, max_delay)
'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Measure the runtime

    Args:
        n (int): The number of execute wait_random()
        max_delay (int): The maximum delay value.

    Returns:
        float: average of execution time for wait_n(n, max_delay)
    '''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    return (end - start) / n
