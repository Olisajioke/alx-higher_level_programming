#!/usr/bin/python3

if __name__ == "__main__":
    '''
        Calling functions for calculation
    '''
    from calculator_1 import (add, sub, mul, div)
    import sys

    def my_calculator(a, operator, b):
        num_of_arg = len(sys.argv)
        if num_of_arg != 4:
            print("Usage: ./100-my_calculator.py <arg1><operator><arg2>\n")
            sys.exit(1)

        a = int(a)
        b = int(b)

        if operator == '+':
            result = add(a, b)
            print("{} + {} = {}".format(a, b, result))
        elif operator == '/':
            result = div(a, b)
            print("{} / {} = {}".format(a, b, result))
        elif operator == '*':
            result = mul(a, b)
            print("{} * {} = {}".format(a, b, result))
        elif operator == '-':
            result = sub(a, b)
            print("{} - {} = {}".format(a, b, result))
        else:
            print("Unknown Operator. Available Operators: +, -, *, and /,\n")
            sys.exit(1)

    arguments = sys.argv[1:]
    my_calculator(*arguments)
