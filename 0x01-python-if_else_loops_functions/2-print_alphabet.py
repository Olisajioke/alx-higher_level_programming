#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    end_char = '\n' if i == ord('z') else ''
    print(chr(i), end=end_char)
