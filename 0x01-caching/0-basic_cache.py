#!/usr/bin/python3
"""
Create a class BasicCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from the BaseCaching module
    """
    def __init__(self):
        """
        initialize the class instance
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        add an item in caching system
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns: item of the key
        None if the key is not in the cache
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
