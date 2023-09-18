#!/usr/bin/python3
"""This module defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class, inheriting from the Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of the Rectangle class.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): The unique identifier for the rectangle.

        Attributes:
            __width (int): The width of the rectangle.
            __height (int): The height of the rectangle.
            __x (int): The x-coordinate of the rectangle's position.
            __y (int): The y-coordinate of the rectangle's position.
            id (int): The unique identifier for the rectangle.
        """
        super().__init__(id)
        self.__width = 0
        self.__height = 0
        self.__x = 0
        self.__y = 0
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns the area of the Rectangle instance.
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with '#' chars, taking into acct x&y.
        The x and y coordinates determine the position of the rectangle.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the Rectangle instance attributes using *args & **kwargs.
        Args:
            *args: Variable no. of arguments in order: id, width, height,x,y.
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
                self.height = args[3]
            if len(args) >= 5:
                self.width = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value
                elif key == 'height':
                    self.height = value
                elif key == 'width':
                    self.width = value

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Rectangle instance.

        Returns:
            dict: A dictionary containing id, width, height, x, and y.
        """
        return {
            'x': self.x,
            'width': self.__width,
            'id': self.id,
            'height': self.__height,
            'y': self.y
        }
