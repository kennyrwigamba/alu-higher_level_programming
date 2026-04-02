#!/usr/bin/python3
"""3. Same class or inherit from module."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclasses."""
    return isinstance(obj, a_class)
