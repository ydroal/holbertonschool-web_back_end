#!/usr/bin/python3
'''FIFOCache module
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' FIFOCache defines:
    '''
    def __init__(self):
        ''' Initiliaze
        '''
        super().__init__()

    def put(self, key, item):
        '''
        Assign to the dictionary self.cache_data the item value
        for the key key
        '''
        if key is None or item is None:
            return
        # 既にキーが存在する場合はアイテムを更新
        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f'DISCARD: {first_key}')
            self.cache_data[key] = item

    def get(self, key):
        ''' Returns the value in self.cache_data linked to key
        '''
        if key is None:
            return None
        else:
            return self.cache_data.get(key)
