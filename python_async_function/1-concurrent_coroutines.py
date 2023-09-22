#!/usr/bin/env python3
'''
Module that contains the asynchronous function wait_n
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
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
    co_list = [wait_random(max_delay) for _ in range(n)]
    for future in asyncio.as_completed(co_list):
        return_value = await future
        result.append(return_value)
    return result
