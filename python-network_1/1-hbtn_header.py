#!/usr/bin/python3
"""Displays the X-Request-Id response header value (urllib)."""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
