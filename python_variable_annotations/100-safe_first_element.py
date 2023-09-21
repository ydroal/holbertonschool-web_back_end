#!/usr/bin/env python3
'''
Module to retrieve the first element of a sequence.
'''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Return a first element of a sequence

    Args:
    lst (sequence): sequences

    Returns:
    Any: The first element of the sequence or None if the sequence is empty.
    '''
    if lst:
        return lst[0]
    else:
        return None
