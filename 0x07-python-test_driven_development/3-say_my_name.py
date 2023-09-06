#!/usr/bin/env python3
"""Define a function to print a person's name."""


def say_my_name(first_name, last_name=""):
    """
    Prints the person's name in the
    format "My name is <first name> <last name>".

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional):
        The last name of the person. Defaults to an empty string.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = f"My name is {first_name} {last_name}"
    print(full_name)
