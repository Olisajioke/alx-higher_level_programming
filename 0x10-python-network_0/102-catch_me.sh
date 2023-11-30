#!/bin/bash
# A bash script to make a request causing the server to respond with "You got me!"
curl -s -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
