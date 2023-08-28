#!/usr/bin/python3

import sys


def execute_safely(func, *arguments):
    """Safely executes a provided function.

    Args:
        func: The function to be executed.
        arguments: Arguments for the function.

    Returns:
        If an exception occurs - None.
        Otherwise - the result of the function call.
    """
    try:
        result = func(*arguments)
        return (result)
    except Exception as e:
        error_message = "An exception occurred: {}".format(e)
        print(error_message, file=sys.stderr)
        return (None)
