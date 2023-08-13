#!/usr/bin/python3
def max_integer(my_list=[]):
    ''' A function to find the maximum integer '''
    if len(my_list) == 0:
        return(None)

    x_max = 0
    for num in my_list:
        if num > x_max:
            x_max = num
    return(x_max)
