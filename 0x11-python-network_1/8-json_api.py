#!/usr/bin/python3
"""
A script that takes in a letter and
sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': letter}

    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        json_data = response.json()
        if json_data:
            user_id = json_data.get('id')
            user_name = json_data.get('name')
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
