#!/usr/bin/env python3
"""Utils module: Utility functions for nested map access, JSON requests, and memoization"""

from typing import Mapping, Any, Sequence, Union, Callable
import requests


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access a nested map using a sequence of keys"""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str) -> Any:
    """Make a GET request and return the JSON content"""
    response = requests.get(url)
    return response.json()


def memoize(method: Callable) -> Callable:
    """Decorator to cache method results"""
    attr_name = "_{}".format(method.__name__)

    @property
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)

    return wrapper
