#!/usr/bin/python3
# 0-add_integer.py
"""
Module for adding two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers and return the result
    """
    try:
        return int(a) + int(b)
    except (ValueError, TypeError):
        if not isinstance(a, (int, float)):
            raise ValueError("a must be an integer or float")
        elif not isinstance(b, (int, float)):
            raise ValueError("b must be an integer or float")
