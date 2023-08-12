#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    '''Checks if idx is out of range or negative'''
    if idx < 0 or idx >= len(my_list):
        return (my_list.copy())
    new_list = my_list[:]
    new_list[idx] = element
    return (new_list)
