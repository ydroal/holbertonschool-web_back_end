#!/usr/bin/python3
'''LIFOCache module
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    ''' LIFOCache defines:
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
        # 既にキーが存在する場合は、それを削除して最後に再追加する
        if key in self.cache_data:
            self.cache_data.pop(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            deleted_element = self.cache_data.popitem()
            deleted_key = deleted_element[0]
            print(f'DISCARD: {deleted_key}')

        self.cache_data[key] = item

    def get(self, key):
        ''' Returns the value in self.cache_data linked to key
        '''
        if key is None:
            return None
        else:
            return self.cache_data.get(key)
