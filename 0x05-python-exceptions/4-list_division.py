#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            value_1 = my_list_1[i] if i < len(my_list_1) else 0
            value_2 = my_list_2[i] if i < len(my_list_2) else 0

            if not isinstance(value_1, (int, float)) or \
               not isinstance(value_2, (int, float)):
                print("wrong type")
                result_list.append(0)
            elif value_2 == 0:
                print("division by 0")
                result_list.append(0)
            else:
                result = value_1 / value_2
                result_list.append(result)
        except IndexError:
            print("out of range")
            result_list.append(0)
        except Exception as e:
            print("An error occurred:", str(e))
            result_list.append(0)

    return result_list
