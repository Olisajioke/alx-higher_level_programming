#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_num = set()
    result = 0
    for item in my_list:
        if item not in unique_num:
            unique_num.add(item)
            result += item
    return(result)
