#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming" \
      " language that combines remarkable power with very clear syntax"
print(str.split()[10][:-1], str.split()[13], str.split()[6][:-1],
      str.split()[8], sep=' ')
