#!/usr/bin/python3
"""This module defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class, inheriting from the Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an instance of the Square class.
        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
            y (int, optional): The y-coordinate of the square's position.
            id (int, optional): The unique identifier for the square.

        Attributes:
            __width (int): The width of the square (inherited from Rectangle).
            __height (int): The height of square (inherited from Rectangle).
            __x (int): The x-coordinate of square's position (from Rectangle).
            __y (int): The y-coordinate of square's position (from Rectangle).
            id (int): The unique identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the Square instance.
        Returns:
            str: A formatted string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Updates the Square instance attributes using *args and **kwargs.
        Args:
            *args: Variable number of arguments in the order: id, size, x, y.
            **kwargs: Arbitrary keyword arguments for attribute updates.
        """
        if args:
            if len(args) >= 1:
                self.x = args[0]
            if len(args) >= 2:
                self.y = args[1]
            if len(args) >= 3:
                self.id = args[2]
            if len(args) >= 4:
                self.size = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value

    def to_dictionary(self):
        """Returns a dictionary representation of the Square instance.
        Returns:
            dict: A dictionary containing id, size, x, and y.
        """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.width,
            'y': self.y
        }
