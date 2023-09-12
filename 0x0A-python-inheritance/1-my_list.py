#!/usr/bin/python3
"""Defines a module that prints a list in asccending order."""


class MyList(list):
    """Implements a module for the built-in list class"""

    def print_sorted(self):
        """This method sorts the list in ascending order and then prints it."""
        sorted_list = sorted(self)
        print(sorted_list)
