#!/usr/bin/python3
"""Displays the X-Request-Id response header value (requests)."""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
