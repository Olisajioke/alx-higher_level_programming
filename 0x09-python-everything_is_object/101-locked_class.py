#!/usr/bin/python3
"""Module that define a locked class"""


class LockedClass:
    """
    A class that prevents the creation of new instance attributes
    except for 'first_name'.
    """

    def __setattr__(self, name, value):
        """
        Override the default setattr method to restrict attribute creation.
        Only 'first_name' attribute can be set.
        """
        if hasattr(self, name):
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{name}'"
            )
        if name != 'first_name':
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{name}'"
            )
        super().__setattr__(name, value)
