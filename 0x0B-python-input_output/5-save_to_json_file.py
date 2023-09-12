#!/usr/bin/python3
"""Defines a function that writes a JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using its JSON representation."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
