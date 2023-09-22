#!/usr/bin/env python3
'''
Module that contains the asynchronous function wait_random
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Waits for a random delay between 0 and max_delay seconds and returns it.

    Args:
    max_delay (int): The maximum delay value. Defaults is 10

    Returns:
        float: The delay value.
    '''

    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
