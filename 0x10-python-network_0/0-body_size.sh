#!/bin/bash
# This script sends a request to a given URL using curl and displays only the size of the response body in bytes

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"
response=$(curl -sI "$url" | grep -i content-length | awk '{print $2}' | tr -d '\r' | tr -d '\n')
echo "$response"
