#!/usr/bin/python3
"""Defines a Student class with attributes and a to_json method."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list of str, optional): A list of
            attribute names to include in the dictionary.
                If None, all attributes will be included.

        Returns:
            dict: A dictionary containing specified attributes of the Student.
        """
        if attrs is None:
            attrs = ['age', 'last_name', 'first_name']

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)

        return result
