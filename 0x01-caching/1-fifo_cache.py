#!/usr/bin/env python3
"""
Defines a FIFO caching system.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Defines a First-In First-Out caching system.
    """

    def __init__(self):
        """
        Initializes the instance.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        Retrieves an item from the cache.
        """
        return self.cache_data.get(key, None)
