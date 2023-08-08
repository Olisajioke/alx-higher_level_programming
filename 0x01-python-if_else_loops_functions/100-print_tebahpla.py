#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    end_char = '\n' if i == ord('a') else ''
    char_to_print = chr(i).lower() if i % 2 == 1 else chr(i).upper()
    print("{}{}".format(char_to_print, end_char), end="")
