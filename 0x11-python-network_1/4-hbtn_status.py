#!/usr/bin/python3
"""A script that fetches https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    content = response.text

    print("- {}\n\t{}".format("Body response:", content))
