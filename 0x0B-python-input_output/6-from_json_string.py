#!/usr/bin/python3
import json


def from_json_string(my_str):
    '''
    returns an object (Python data structure)
    '''
    return json.loads(my_str)
