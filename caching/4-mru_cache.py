#!/usr/bin/python3
'''MRUCache module
'''
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    ''' MRUCache defines:
    '''
    def __init__(self):
        ''' Initiliaze
        '''
        super().__init__()
        self.od = OrderedDict()

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
            self.od.move_to_end(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            recent_key = next(iter(self.od))
            self.cache_data.pop(recent_key)
            self.od.pop(recent_key)
            print(f'DISCARD: {recent_key}')

        self.cache_data[key] = item
        # キーだけodに登録。値は無視
        self.od[key] = None
        self.od.move_to_end(key, False)

    def get(self, key):
        ''' Returns the value in self.cache_data linked to key
        '''
        if key is None or key not in self.cache_data:
            return None
        else:
            self.od.move_to_end(key, False)
            return self.cache_data.get(key)
