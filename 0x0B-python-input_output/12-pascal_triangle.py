#!/usr/bin/python3
"""Generates Pascal's triangle up to the nth row."""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row.

    Returns a list of integers.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)
        triangle.append(row)

    return triangle
