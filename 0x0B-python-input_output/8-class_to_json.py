#!/usr/bin/python3
"""Converts an object to a dictionary representation for JSON serialization."""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure."""
    return obj.__dict__
