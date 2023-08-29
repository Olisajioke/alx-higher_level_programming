#!/usr/bin/python3
"""Module that creates a square class"""


class Square:
    """A class representing a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance.
        area(self): Calculates the area of the square.
        my_print(self): Prints the square using '#'.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square (default is 0).
        """
        self.size = size  # Use the setter to perform validation

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

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#'.

        Prints a square made of '#' characters with the given size.
        If size is 0, a blank line is printed.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
