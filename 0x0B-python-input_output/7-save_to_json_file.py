#!/usr/bin/python3
import json
"""writes an Object to a text file, using a JSON rep
"""


def save_to_json_file(my_obj, filename):
    with open(filename, mode='w') as File:
        json.dump(my_obj, File)
