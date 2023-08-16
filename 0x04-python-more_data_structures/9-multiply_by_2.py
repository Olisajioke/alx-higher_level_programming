#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    key_list = list(new_dict.keys())

    for key in key_list:
        new_dict[key] *= 2

    return (new_dict)
