#!/usr/bin/python3
"""Return a dictionary description of an object for JSON serialization."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization of obj."""
    return obj.__dict__
