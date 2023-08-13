#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    ''' A function that lists numbers that are divisible by 2'''
    result = []
    for x in range(len(my_list)):
        if x % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return (result)
