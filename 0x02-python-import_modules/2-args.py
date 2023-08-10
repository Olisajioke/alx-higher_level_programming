#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of arguements,


        And list ofarguments.
    """
    import sys

    argv_count = len(sys.argv) - 1
    if argv_count == 0:
        print("0 arguments.")
    elif argv_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argv_count))
    for x in range(argv_count):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
