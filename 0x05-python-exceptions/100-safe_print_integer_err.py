#!/usr/bin/python3

import sys


def safe_print_integer_err(num):
    """Prints an integer using "{:d}".format().

    In case of a ValueError,appropriate error message is printed to standerr

    Args:
        num (int): The integer to be printed.

    Returns:
        If an exception occurs (TypeError or ValueError) - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(num))
        return (True)
    except (ValueError, IndexError):
        error_message = "An error occurred: {}".format(sys.exc_info()[1])
        print(error_message, file=sys.stderr)
        return (False)
