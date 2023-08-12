#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Function that replaces an element of a list at a specific position."""
    if 0 <= idx < len(my_list):
        my_list[idx] = element
        return (my_list)
