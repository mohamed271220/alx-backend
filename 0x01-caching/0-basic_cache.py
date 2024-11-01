#!/usr/bin/env python3
"""
    basic cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    class that inherit from BaseCaching
    """

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key, None)
