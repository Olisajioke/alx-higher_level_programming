#!/usr/bin/python3
"""
models/base.py: Contains the Base class for managing id attributes.
"""


class Base:
    """The Base class manages id attribute for all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of Base.

        Args:
            id (int, optional): The id for this instance. If not provided,
            it will be automatically generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
