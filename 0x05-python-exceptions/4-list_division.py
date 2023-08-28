#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            e1 = my_list_1[i] if i < len(my_list_1) else 0
            e2 = my_list_2[i] if i < len(my_list_2) else 0

            if isinstance(e1, (int, float)) and isinstance(e2, (int, float)):
                if e2 != 0:
                    division_result = e1 / e2
                    result.append(division_result)
                else:
                    result.append(0)
                    print("division by 0")
            else:
                result.append(0)
                print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")

    return result
