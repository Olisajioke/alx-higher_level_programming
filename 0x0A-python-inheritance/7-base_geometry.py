#!/usr/bin/python3
"""Defines a class that operates geometry-related operations"""


class BaseGeometry:
    """This is a base class for geometry-related operations."""

    def area(self):
        """Calculate the area of the geometry objects"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value as an integer and check if it's greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
