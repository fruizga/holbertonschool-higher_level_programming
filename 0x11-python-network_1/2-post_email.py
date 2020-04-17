#!/usr/bin/python3
""" Takes in a URL and an email, sends a POST request to
    the passed URL with the email as a parameter
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
