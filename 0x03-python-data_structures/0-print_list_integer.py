#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """function that prints all integers of a list."""
    for num in range(len(my_list)):
        print("{:d}".format(my_list[num]))
