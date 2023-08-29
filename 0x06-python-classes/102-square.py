#!/usr/bin/python3
"""This module defines a class Square that represents a square."""


class Square:
    """A class representing a square.

    Attributes:
        size (int or float): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance.
        area(self): Calculates the area of the square.
        __eq__(self, other): Checks if two squares are equal in area.
        __ne__(self, other): Checks if two squares are not equal in area.
        __gt__(self, other):
        Checks if one square's area is greater than the other's.
        __ge__(self, other):
        Checks if one square's area is greater than or equal to the other's.
        __lt__(self, other):
        Checks if one square's area is less than the other's.
        __le__(self, other):
        Checks if one square's area is less than or equal to the other's.

    Raises:
        TypeError: If size is not a number.
        ValueError: If size is less than 0.
    """
    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int or float, optional):
            The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """int or float: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int or float): The size of the square.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal in area.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal in area.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if one square's area is greater than the other's.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square's area is greater than or equal to the other's.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if the area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if one square's area is less than the other's.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square's area is less than or equal to the other's.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if the area is less or equal, False otherwise.
        """
        return self.area() <= other.area()
