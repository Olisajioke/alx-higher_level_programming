#!/bin/bash
# A bash script to send a JSON POST request to a URL and display the response body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
