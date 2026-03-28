#!/usr/bin/python3
"""Defines a Square class with size property and area method."""


class Square:
    """Represents a square with validated size via property."""

    def __init__(self, size=0):
        """Initialize a Square with optional validated size."""
        self.size = size

    @property
    def size(self):
        """Get the current square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square size with type and value validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
