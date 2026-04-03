#!/usr/bin/python3
"""A script tha:
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    response = requests.post(
        "http://0.0.0.0:5000/search_user",
        data={"q": q},
    )

    try:
        data = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
