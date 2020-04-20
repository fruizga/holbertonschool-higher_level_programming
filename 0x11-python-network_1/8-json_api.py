#!/usr/bin/python3
""" takes in a letter and sends a POST with the letter as a parameter """
import sys
import requests

if __name__ == "__main__":
    try:
        q = argv[1]
    except:
        q = ''
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}
    r = requests.post(url, payload)
    try:
        json = r.json()
        if len(json) == 0:
            print('No result')
        else:
            json_id = json.get('id')
            json_name = json.get('name')
            print('[{}] {}'.format(json_id, json_name))
    except:
        print('Not a valid JSON')
