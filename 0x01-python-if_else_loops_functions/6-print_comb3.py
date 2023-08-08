#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        end_char = "\n" if i == 8 and j == 9 else ", "
        print("{:02d}".format(i), "{:02d}".format(j), sep=", ", end=end_char)
