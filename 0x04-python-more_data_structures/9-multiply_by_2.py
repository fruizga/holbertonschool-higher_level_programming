#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDictio = a_dictionary.copy()
    for key, value in newDictio.items():
        newDictio[key] = value * 2
    return newDictio
