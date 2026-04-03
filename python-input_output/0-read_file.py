#!/usr/bin/python3
"""Read and print a text file (UTF-8)."""


def read_file(filename=""):
    """Read a text file (UTF-8) and print it to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
