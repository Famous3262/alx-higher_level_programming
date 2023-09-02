#!/usr/bin/python3
"""A script that takes in a URL,
sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

# Create a dictionary with the email as a parameter
    data = {'email': email}

# Send a POST request to the URL with the data
    response = requests.post(url, data=data)
    print(response.text)
