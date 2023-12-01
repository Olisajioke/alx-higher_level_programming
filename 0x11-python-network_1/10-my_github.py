#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a letter as
Displays the id and name if JSON is properly formatted and not empty.
Handles various response scenarios.
"""

import requests
import sys

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    page = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = page.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("None")
