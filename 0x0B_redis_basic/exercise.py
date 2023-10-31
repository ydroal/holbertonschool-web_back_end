#!/usr/bin/env python3
"""
Cache class Module
"""
import redis
import uuid
from typing import Union


class Cache():
    """ Define Cache class
    """
    def __init__(self):
        """ Initialize a Cace instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)

        return random_key
