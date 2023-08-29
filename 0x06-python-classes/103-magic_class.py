#!/usr/bin/python3
"""This module explains bytecode and defines a MagicClass."""


import math


class MagicClass:
    """A class that calculates area and circumference based on radius.

    Attributes:
        radius (int or float): The radius of the circle.

    Methods:
        __init__(self, radius): Initializes a new MagicClass instance.
        area(self): Calculates the area of the circle.
        circumference(self): Calculates the circumference of the circle.

    Raises:
        TypeError: If radius is not a number.
    """
    def __init__(self, radius):
        """Initialize a new MagicClass instance.

        Args:
            radius (int or float): The radius of the circle.
        """
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        """int or float: The radius of the circle."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Set the radius of the circle.

        Args:
            value (int or float): The radius of the circle.

        Raises:
            TypeError: If value is not a number.
        """
        if not isinstance(value, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = value

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
