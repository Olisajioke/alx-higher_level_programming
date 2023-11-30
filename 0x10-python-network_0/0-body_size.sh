#!/bin/bash
# This script sends a request to a given URL using curl and displays only the size of the response body 
curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r\n'
