#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    ''' Function that returns different elements present in a list'''
    diff_element = set()

    for item in set_1:
        if item not in set_2:
            diff_element.add(item)

    for item in set_2:
        if item not in set_1:
            diff_element.add(item)

    return(diff_element)
