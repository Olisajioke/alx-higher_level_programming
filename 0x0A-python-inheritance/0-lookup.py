#!/usr/bin/env python3
"""A module that defines an object attribute lookup function"""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    attributes_and_methods = []
    for name in dir(obj):
        if callable(getattr(obj, name)) or hasattr(obj, name):
            attributes_and_methods.append(name)
    return attributes_and_methods
