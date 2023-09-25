#!/usr/bin/env python3
'''
Module that yield a random number between 0 and 10 asynchronously
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Asynchronously yield random numbers.

    This coroutine will loop 10 times. Each iteration, it will
    wait for 1 second and then yield a random number between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
