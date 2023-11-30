#!/bin/bash
# A bash script to send a POST request to a URL with predefined data using curl
data="email=test@gmail.com&subject=I will always be here for PLD"
curl -s -X POST -d "$data" "$1"
