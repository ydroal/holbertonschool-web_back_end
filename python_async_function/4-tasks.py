#!/usr/bin/env python3
'''
Module that coroutines(wait_random()) concurrently and return their results
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Execute coroutines(wait_random()) concurrently and return their results.

    Args:
        n (int): The number of execute wait_random()
        max_delay (int): The maximum delay value.

    Returns:
        List[float]: A list of delay values via coroutines,
        in the order they completed.
    '''
    result = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        completed_result = await task
        result.append(completed_result)
    return result
