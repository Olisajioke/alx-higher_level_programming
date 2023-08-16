#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = [replace if item == search else item for item in my_list]
    print(my_list)
