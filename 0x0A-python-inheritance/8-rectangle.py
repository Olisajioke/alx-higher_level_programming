#!/usr/bin/python3
"""Defines a class for geometry-related operations"""


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle with specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
