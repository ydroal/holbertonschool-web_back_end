#!/usr/bin/env python3
'''
Module to adding up the elements of a list.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    adding up the elements of a list.

    Args:
    mxd_lst (int, float): list of int and float

    Returns:
    float: sum of elements of a list.
    '''

    return sum(mxd_lst)
