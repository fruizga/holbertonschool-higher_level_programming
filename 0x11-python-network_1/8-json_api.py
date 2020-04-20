#!/usr/bin/python3
""" takes in a letter and sends a POST with the letter as a parameter """
from sys import argv
import requests

if __name__ == "__main__":
    a = argv[1] if len(argv) > 1 else ""
    try:
        req = requests.post('http://0.0.0.0:5000/search_user\
        ', data={'a': a}).json()
        print("[{}] {}".format(req['id'], R1['name'])
              if 'id' in req and 'name' in req else "No result")
    except ValueError:
        print("Not a valid JSON")
