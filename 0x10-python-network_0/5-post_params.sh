#!/bin/bash
# A bash script to send a POST request with predefined data to a URL using curl
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
