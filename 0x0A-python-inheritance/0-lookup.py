#!/usr/bin/env python3


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
    obj (object): The object to inspect.

    Returns:
    list: A list containing the names of attributes and methods.
    """
    attributes_and_methods = []
    for name in dir(obj):
        if callable(getattr(obj, name)) or hasattr(obj, name):
            attributes_and_methods.append(name)
    return attributes_and_methods
