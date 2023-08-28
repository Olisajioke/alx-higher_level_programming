#!/usr/bin/python3

def safe_print_division(num1, num2):
    """Computes the division of num1 by num2 and return the result."""
    result = None
    try:
        result = num1 / num2
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Computed result: {}".format(result))
    return (result)
