#!/usr/bin/env python3

class BaseGeometry:
    """
    This is a base class for geometry-related operations.
    """

    def area(self):
        """
        Calculate the area of the geometry object.

        Raises:
        Exception: This method should be implemented in subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as an integer and check if it's greater than 0.

        Args:
        name (str): The name of the value being validated.
        value (int): The value to be validated.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
