#!/usr/bin/python3
"""Module that defines MyList, a list subclass with sorted display."""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
