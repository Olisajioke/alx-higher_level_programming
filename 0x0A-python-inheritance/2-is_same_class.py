#!/usr/bin/env python3
"""A modules that defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
    obj (object): The object to check.
    a_class (class): The class to compare with.

    Returns:
    bool: True if obj is an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
