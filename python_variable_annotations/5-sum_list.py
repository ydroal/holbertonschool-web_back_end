#!/usr/bin/env python3
'''
Module to adding up the elements of a list.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    adding up the elements of a list.

    Args:
    input_list (float): list of floats

    Returns:
    float: sum of elements of a list.
    '''

    return sum(input_list)
