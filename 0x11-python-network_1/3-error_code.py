#!/usr/bin/python3
"""
Sends a request to a URL & displays the body of the response, handles errors
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            decoded_response = response.read().decode('utf-8')
            print(decoded_response)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
