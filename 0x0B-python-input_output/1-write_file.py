#!/usr/bin/python3
"""Defines a function that writes a file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            return file.write(text)
    except Exception as e:
        return 0
