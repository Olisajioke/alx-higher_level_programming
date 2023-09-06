#!/usr/bin/env python3
"""Define a function to format text."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    formatted_text = ""
    skip_newline = False

    for char in text:
        if char in [".", "?", ":"]:
            formatted_text += char + "\n\n"
            skip_newline = True
        else:
            if char == " " and skip_newline:
                continue
            formatted_text += char
            skip_newline = False

    print(formatted_text)
