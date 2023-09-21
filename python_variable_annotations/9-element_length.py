#!/usr/bin/env python3
'''
Module to compute element lengths in a list.
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Return a list of tuples, each containing an element of argument
    and its length.

    Args:
    lst (sequence): An iterable of sequences

    Returns:
    list: List of tuples with an element from the lst and its length.
    '''
    return [(i, len(i)) for i in lst]
