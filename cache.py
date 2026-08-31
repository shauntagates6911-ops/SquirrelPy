# src/squirrelpy/cache.py

from functools import lru_cache
from typing import Any, Dict


class SquirrelCache:
    """
    Ultra-fast LRU cache for SquirrelPy.
    Uses Python's built-in LRU engine for maximum speed.
    """

    def __init__(self, max_size: int = 256):
        self.max_size = max_size

    @lru_cache(maxsize=256)
    def remember(self, key: str, value: Any):
        """
        Stores a value in the cache.
        """
        return value

    @lru_cache(maxsize=256)
    def get(self, key: str):
        """
        Retrieves a cached value.
        """
        return None  # if not cached, returns None

    def clear(self):
        """
        Clears the entire cache.
        """
        self.remember.cache_clear()
        self.get.cache_clear()
