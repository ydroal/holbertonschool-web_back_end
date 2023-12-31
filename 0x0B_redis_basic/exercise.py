#!/usr/bin/env python3
"""
Cache class Module
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs of store method
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function
        """
        input_key = f'{method.__qualname__}:inputs'
        output_key = f'{method.__qualname__}:outputs'
        random_key = method(self, *args, **kwargs)
        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, random_key)
        return random_key
    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a store method is called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def replay(method: Callable):
    """
    Display the history of calls of a particular function
    """
    cache = method.__self__
    method_name = method.__qualname__
    print(f'{method_name} was called {int(cache.get(method_name))} times:')
    input_key = f'{method_name}:inputs'
    output_key = f'{method_name}:outputs'
    inputs = cache._redis.lrange(input_key, 0, -1)
    outputs = cache._redis.lrange(output_key, 0, -1)

    for input, output in zip(inputs, outputs):
        print(f'{method_name}(*{input.decode()}) -> {output.decode()}')


class Cache():
    """ Define Cache class
    """
    def __init__(self):
        """ Initialize a Cache instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data using a random generated key
        """
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
