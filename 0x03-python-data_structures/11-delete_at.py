#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    ''' Function that deletes an item at a particular idex '''
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        del my_list[idx]

    return (my_list)
