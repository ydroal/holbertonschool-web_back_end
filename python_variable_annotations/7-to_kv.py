#!/usr/bin/env python3
'''
Module to return the tuple of string and square of the int/float.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    return the tuple of string and square of the int/float.

    Args:
    k (str): string to return
    v (int or float): given number

    Returns:
    tuple: string and square of the int/float
    '''

    return (k, float(v*v))
