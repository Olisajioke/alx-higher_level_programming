#!/usr/bin/python3
"""Defines a class that raises area exceptions"""


class BaseGeometry:
    """This is a base class for geometry-related operations."""

    def area(self):
        """Exception: This method should be implemented in subclasses."""
        raise Exception("area() is not implemented")
