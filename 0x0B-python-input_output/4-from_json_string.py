#!/usr/bin/python3
"""Defines a function that writes a JSON-to-object."""
import json


def from_json_string(my_str):
    """Return a Python data structure (object) represented by a JSON string."""
    return json.loads(my_str)
