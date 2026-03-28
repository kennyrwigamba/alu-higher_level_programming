#!/usr/bin/python3
""" Defines a Square class with size and position properties. """


class Square:
    """ Represents a square that can be printed at a given position. """

    def __init__(self, size=0, position=(0, 0)):
        # Initialize a Square with optional size and position.
        self.size = size
        self.position = position

    @property
    def size(self):
        # Get the current square size.
        return self.__size

    @size.setter
    def size(self, value):
        # Set square size with type and value validation.
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        # Get the current square position.
        return self.__position

    @position.setter
    def position(self, value):
        # Set square position with tuple validation.
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        # Return the area of the square.
        return self.__size**2

    def my_print(self):
        # Print the square using # and applying position offsets.
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print((" " * self.__position[0]) + ("#" * self.__size))
