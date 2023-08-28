#!/usr/bin/python3

def perform_elementwise_division(list_1, list_2, length_of_list):
    """Function that divides elements of two lists element by element.

    Args:
        list_1 (list): The initial list.
        list_2 (list): The secondary list.
        length_of_list (int): The count of elements to divide.

    Returns:
        New list: length_of_list containing the element-wise divisions.
    """
    divided_list = []
    for idx in range(0, length_of_list):
        try:
            result = list_1[idx] / list_2[idx]
        except TypeError:
            print("invalid data type")
            result = 0
        except ZeroDivisionError:
            print("division by zero")
            result = 0
        except IndexError:
            print("index out of range")
            result = 0
        finally:
            divided_list.append(result)
    return (divided_list)
