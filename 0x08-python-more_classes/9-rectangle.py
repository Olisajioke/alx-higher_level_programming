#!/usr/bin/python3
"""Module that defines a Rectangle class."""


class Rectangle:
    """Rectangle class to define and handle rectangles."""

    number_of_instances = 0  # Public class attribute
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the instance count

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string with the rectangle
            represented by print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        row = str(self.print_symbol) * self.__width
        return "\n".join([row] * self.__height)

    def __repr__(self):
        """Return a string representation of the object.

        Returns:
            str: A string representation that can
            recreate the object using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        Rectangle.number_of_instances -= 1  # Decrement the instance count
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on the area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If either rect_1
            or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the
            greater area or rect_1 if they have the same area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a new Rectangle instance as a square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Returns:
            Rectangle: A new Rectangle
            instance with width and height equal to size.
        """
        return cls(size, size)
