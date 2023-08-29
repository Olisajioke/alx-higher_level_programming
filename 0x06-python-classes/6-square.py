#!/usr/bin/python3
"""This module defines a class Square that represents a square."""


class Square:
    """A class representing a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)):
        Initializes a new Square instance.
        area(self): Calculates the area of the square.
        my_print(self): Prints the square using '#'.

    Raises:
        TypeError: If size or position is not of the correct type.
        ValueError: If size or position has invalid values.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square (default is 0).
            position (tuple, optional):
            The position of the square (default is (0, 0)).
        """
        self.size = size  # Use the setter to validate
        self.position = position

    @property
    def size(self):
        """int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: The position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(val, int) for val in value) or
                any(val < 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#'.

        Prints a square made of '#' characters with given size, position.
        If size is 0, a blank line is printed.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
