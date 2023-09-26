#!/usr/bin/env python3
'''
Module that calculate the start and end indexes
for pagination based on the provided page number and page size
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    '''
    Calculate the start and end indexes for pagination.

    Args:
        page (int): The page number (start from 1)
        page_size (int): The number of items per page


    Returns:
        Tuple: size two containing a start index and an end index
    '''

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
