#!/usr/bin/env python3

class MyList(list):
    def print_sorted(self):
        """
        Print the list in ascending sorted order.

        This method sorts the list in ascending order and then prints it.
        """
        sorted_list = sorted(self)
        print(sorted_list)
