#!/usr/bin/python3

def safe_print_integer(val):
    """Function that Prints an integer with "{:d}".format().

    Args:
        val (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - function returns False.
        it returns True.
    """
    try:
        format_str = "{:d}"
        formatted_val = format_str.format(val)
        print(formatted_val)
        return (True)
    except (ValueError, KeyError):
        return (False)
