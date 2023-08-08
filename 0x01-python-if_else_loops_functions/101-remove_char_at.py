#!/usr/bin/python3
def remove_char_at(s, n):
    new_str = ""
    for i in range(len(s)):
        if i != n:
            new_str += s[i]
    return new_str
