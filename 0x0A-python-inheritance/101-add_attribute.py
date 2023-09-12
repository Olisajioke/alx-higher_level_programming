#!/usr/bin/env python3

def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if it's possible.

    Args:
    obj: The object to which the attribute will be added.
    attr_name (str): The name of the attribute.
    attr_value: The value of the attribute.

    Raises:
    TypeError: If the object cannot have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr_name] = attr_value
