#!/usr/bin/env python3
'''
Module that measures the total runtime for executing
`async_comprehension` coroutine four times in parallel.
'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measure the runtime of executing `async_comprehension` four times
    in parallel using asyncio.gather.

    Returns:
        float: Total runtime in seconds.
    '''
    co_list = [async_comprehension() for _ in range(4)]
    start = time.time()
    # asyncio.gatherは可変長の引数を受け取るのでリストをそのまま渡すのではなく
    # アンパックして個別のコルーチンとして渡す
    await asyncio.gather(*co_list)
    end = time.time()

    return end - start
