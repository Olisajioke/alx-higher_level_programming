#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == '':
        return(None)

    max_integer = 0
    for num in my_list:
        if num > max_integer:
            max_integer = num
    return (max_integer)
