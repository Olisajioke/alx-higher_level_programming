#!/usr/bin/env python3

def no_c(my_string):
    """Function that removes all the c and C in a string"""
    new_string = ''
    for char in my_string:
        if char != "c" and char != "C":
            new_string += char
    return (new_string)
