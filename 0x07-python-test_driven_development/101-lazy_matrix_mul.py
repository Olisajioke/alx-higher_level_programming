#!/usr/bin/env python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy and returns the result.

    Args:
        m_a (numpy.ndarray): The first matrix as a NumPy array.
        m_b (numpy.ndarray): The second matrix as a NumPy array.

    Raises:
        ValueError: If the matrices cannot be multiplied due to shape mismatch.

    Returns:
        numpy.ndarray: The resulting matrix after multiplication.
    """
    try:
        result = np.dot(m_a, m_b)
        return result
    except ValueError as e:
        raise ValueError("Matrix multiplication error: " + str(e))
