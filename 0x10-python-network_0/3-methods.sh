#!/bin/bash
# Display all HTTP methods the server will accept
curl -s -I "$1" | grep -i 'allow:' | awk '{print substr($0, 8)}'
