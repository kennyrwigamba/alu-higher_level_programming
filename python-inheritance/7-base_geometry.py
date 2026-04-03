#!/usr/bin/python3
"""Module defines BaseGeometry class with integer validation helpers."""


class BaseGeometry:
    """Represent base geometry operations."""

    def area(self):
        """Raise exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
