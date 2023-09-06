#!/usr/bin/env python3
"""
Matrix Multiplication Function.

This module defines a function to multiply two matrices with given validation
requirements.
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices and return the result.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists, empty,
                   or contains non-integer/non-float elements.
        ValueError: If m_a and m_b cannot be multiplied due to shape mismatch.

    Returns:
        list of lists: The resulting matrix after multiplication.
    """
    # Check if m_a is a list of lists
    if (not isinstance(m_a, list) or
            not all(isinstance(row, list) for row in m_a)):
        raise TypeError("m_a must be a list of lists")

    # Check if m_b is a list of lists
    if (not isinstance(m_b, list) or
            not all(isinstance(row, list) for row in m_b)):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Check if m_a contains only integers or floats
    for row in m_a:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_a should contain only integers or floats")

    # Check if m_b contains only integers or floats
    for row in m_b:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_b should contain only integers or floats")

    # Check if m_a and m_b have matching dimensions for multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
