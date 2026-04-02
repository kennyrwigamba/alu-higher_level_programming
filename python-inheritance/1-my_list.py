#!/usr/bin/python3
"""1. MyList module."""


class MyList(list):
    """A list subclass with a sorted-print helper."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
