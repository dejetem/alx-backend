#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from
BaseCaching and is a caching system:
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    inheriting from BaseCache class
    """
    def __init__(self):
        """
        initialize the class instance
        """
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        add an item in caching system
        Args:
            key(str): key of the item
            item: item to add
        Returns: None
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key_2nd_last = len(self.cache_data_list) - 2
                key_last = self.cache_data_list.pop(key_2nd_last)
                del self.cache_data[key_last]
                print("DISCARD: {}".format(key_last))

    def get(self, key):
        """
        get an item from cache
        Args:
            key(str): key of the item
        Returns: item if the key exists, None otherwise
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
