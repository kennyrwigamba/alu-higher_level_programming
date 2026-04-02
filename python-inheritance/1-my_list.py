#!/usr/bin/python3
"""Module that defines MyList, a list subclass with sorted display."""


class MyList(list):
    """Custom list class with a method to print a sorted copy."""

    def print_sorted(self):
        """Print the list elements in ascending sorted order."""
        print(sorted(self))
