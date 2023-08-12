#!/usr/bin/python3

def no_c(my_string):
    """Function that removes all characters c and C from a string."""
    chars = [char for char in my_string if char != 'c' and char != 'C']
    return (''.join(chars))
