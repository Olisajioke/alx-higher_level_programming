#!/usr/bin/python3
"""Sends a request to a URL and displays the value of the X-Request-Id var."""
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
