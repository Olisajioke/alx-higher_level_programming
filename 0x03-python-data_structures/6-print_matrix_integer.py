#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    '''A function that prints a matrix of integers'''
    for row in matrix:
        for value in row:
            print("{:d}".format(value), end=" " if value != row[-1] else "")
        print()
