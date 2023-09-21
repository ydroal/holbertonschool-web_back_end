#!/usr/bin/env python3
'''
Module to retrieve a value of dictionary..
'''
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
) -> Union[Any, T]:
    '''
    Retrieve a value of the dictionary.

    Args:
    dct (Mapping): The dictionary to retrieve the value from
    key (Any): The key for retrieve the value in the dictionary.
    default (Union[T, None]): default value

    Returns:
    Union[Any, T]: The value of the dictionary or the default value(None).
    '''
    if key in dct:
        return dct[key]
    else:
        return default
