#!/usr/bin/python3
"""
A script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as parameter
and finally displays the body of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) != 3:
    print("Usage: python script.py <url> <email>")
    sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={'email': email})

    print(response.text)
