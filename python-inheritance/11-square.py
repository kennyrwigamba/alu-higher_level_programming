#!/usr/bin/python3
"""11. Square #2 module."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class with custom string representation."""

    def __init__(self, size):
        """Initialize square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the square area."""
        return self.__size * self.__size

    def __str__(self):
        """Return [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
