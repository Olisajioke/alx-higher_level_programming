#!/usr/bin/python3
def max_integer(my_list=[]):
    ''' A function to find the maximum integer '''
    if len(my_list) == 0:
        return(None)

    max_integer = 0
    for num in my_list:
        if num > max_integer:
            max_integer = num
    return (max_integer)
