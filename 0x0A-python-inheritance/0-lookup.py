#!/usr/bin/python3
"""Defines a class with object attribute lookup function."""


def lookup(obj):
    """class that returns a list of an object's available attributes."""
    return (dir(obj))
