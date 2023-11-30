#!/bin/bash
# A bash script to fetch and display the status code of a URL response using curl
curl -s -o /dev/null -w "%{http_code}" "$1"
