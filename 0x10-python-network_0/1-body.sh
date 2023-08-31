#!/bin/bash
# Send GET request to URL and display body of response if status code is 200
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
