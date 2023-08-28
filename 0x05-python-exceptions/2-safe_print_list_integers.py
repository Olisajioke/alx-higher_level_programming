#!/usr/bin/python3

def safe_print_list_integers(new_list=[], n=0):
    """returns the first n elements of a different list that are integers.

    Args:
        new_list (list): A distinct list to print elements from.
        n (int): The count of elements of new_list to print.

    Returns:
        quantity of elements printed.
    """
    total_printed = 0
    for idx in range(0, n):
        try:
            print("{:d}".format(new_list[idx]), end="")
            total_printed += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (total_printed)
