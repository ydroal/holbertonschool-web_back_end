#!/usr/bin/env python3
'''
Module that create the task of coroutine to run concurrently
'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Create the task for wait_random to run concurrently

    Args:
        max_delay (int): The maximum delay value.

    Returns:
        asyncio.Task: An Task object
    '''
    # asyncio.create_task() はコルーチンをタスクとしてスケジュールし、
    # すぐにそのタスクの実行を開始する
    task = asyncio.create_task(wait_random(max_delay))
    return task
