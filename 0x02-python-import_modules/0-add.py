#!/usr/bin/python3

if __name__ == '__main__':
    """My addition function
        adds two numbers together using function
        imported from add.0
    """
    from add_0 import add

a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))
