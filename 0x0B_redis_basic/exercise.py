#!/usr/bin/env python3
"""
Cache class Module
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decolator to count the number of times a store method is called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """ Define Cache class
    """
    def __init__(self):
        """ Initialize a Cace instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)

        return random_key

    def get_str(self, data: bytes) -> str:
        """ Convert data to string
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Convert data to int
        """
        return int(data.decode('utf-8'))

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float]:
        """ Convert the data back to the desired format
        """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)
