#!/usr/bin/env python3
""" Utility functions for testing """

import requests
from typing import Mapping, Sequence, Any
from functools import wraps


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access nested map with path"""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str) -> Any:
    """Get JSON content from a URL"""
    response = requests.get(url)
    return response.json()


def memoize(fn):
    """Memoization decorator"""
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return wrapper
