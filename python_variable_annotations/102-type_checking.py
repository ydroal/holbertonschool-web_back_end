#!/usr/bin/env python3
'''
Module to retrieve specified number of value in tupple.
'''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''
    Retrieve specified number of value in tupple.

    Args:
    lst (Tuple): The Tuple to retrieve the value from
    factor (int): number of element to retrieve from Tuple

    Returns:
    List: The value of the Tuple.
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
