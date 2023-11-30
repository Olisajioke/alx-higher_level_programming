#!/bin/bash
# A bash script to fetch the body of a URL response with a custom header using curl
curl -sH "X-School-User-Id: 98" -X GET "$1"
