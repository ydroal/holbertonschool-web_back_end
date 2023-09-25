#!/usr/bin/env python3
'''
Module that collects 10 random numbers asynchronously using
an async comprehension.
'''
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Collect 10 random numbers using async_generator.

    This coroutine will use async comprehension to collect 10 numbers
    asynchronously yielded by the async_generator function.

    Returns:
        list[float]: A list containing 10 random numbers.
    '''
    result = []
    async for i in async_generator():
        result.append(i)
    return result
