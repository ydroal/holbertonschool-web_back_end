#!/usr/bin/env python3
'''
Module to return returns a function that multiplies a float.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Returns a function that multiplies a float by multiplier.

    Args:
    multiplier (float): string to return

    Returns:
    function: function that multiplies a float by multiplier
    '''
    def f(x: float) -> float:
        return x * multiplier

    return f
