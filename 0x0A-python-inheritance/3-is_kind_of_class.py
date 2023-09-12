#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of,
    or inherited from, the specified class.

    Args:
    obj (object): The object to check.
    a_class (class): The class to compare with.

    Returns:
    bool: True if obj is an instance of a_class
    or inherited from it, otherwise False.
    """
    return isinstance(obj, a_class)
