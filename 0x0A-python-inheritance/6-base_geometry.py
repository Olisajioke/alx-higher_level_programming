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
