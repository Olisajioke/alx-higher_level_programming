#!/usr/bin/python3

def trigger_named_error(message=""):
    """Cause a NameError exception with a specified message."""
    raise NameError(message)
