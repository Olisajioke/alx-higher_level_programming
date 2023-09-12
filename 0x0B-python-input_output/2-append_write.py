#!/usr/bin/python3
"""Defines a function that appends a file"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            char_count = file.write(text)
            return char_count
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0
