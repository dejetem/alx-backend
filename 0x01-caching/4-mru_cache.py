#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from
BaseCaching and is a caching system:
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
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
            if key not in self.cache_data_list:
                self.cache_data_list.append(key)
            else:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removed = self.cache_data_list.pop(-2)
                del self.cache_data[removed]
                print("DISCARD: {}".format(removed))

    def get(self, key):
        """
        get an item from cache
        Args:
            key(str): key of the item
        Returns: item if the key exists, None otherwise
        """
        if key:
            if key in self.cache_data:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
                return self.cache_data[key]
        return None
