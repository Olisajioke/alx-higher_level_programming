#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Changes int operators == and !=."""

    def __eq__(self, other):
        """Override the equality operator (==) to invert its behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=) to invert its behavior."""
        return super().__eq__(other)
