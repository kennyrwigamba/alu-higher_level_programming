#!/usr/bin/python3
"""Write a string to a text file (UTF-8)."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF-8) and return chars written."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
