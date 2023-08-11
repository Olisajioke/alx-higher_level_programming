#!/usr/bin/python3
def infiniteAdd(*args):
    '''
        calculates an infinite amount of number
    '''
    total = sum(int(arg) for arg in args)
    print(total)


if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    infiniteAdd(*arguments)
