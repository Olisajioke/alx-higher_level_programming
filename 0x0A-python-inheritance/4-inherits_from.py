#!/usr/bin/python3
"""Defines a class that checks for subclass"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare with.

    Returns:
        bool: True if obj is an instance of a
        subclass of a_class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
