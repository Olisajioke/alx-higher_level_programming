#!/bin/bash
# A bash script to display allowed HTTP methods for a URL using curl
curl -sIX OPTIONS "$1" | awk '/Allow:/ {print substr($0, 8)}'
