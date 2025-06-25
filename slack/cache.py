# Simple in-memory cache implementation
_cache = {}

def get(key):
    """Get a value from cache"""
    return _cache.get(key)

def set(key, value):
    """Set a value in cache"""
    _cache[key] = value

def clear():
    """Clear the cache"""
    _cache.clear()
