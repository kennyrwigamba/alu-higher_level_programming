#!/usr/bin/python3
"""6. Improve geometry module."""


class BaseGeometry:
    """Base geometry class with abstract area behavior."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")
