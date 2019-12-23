#!/usr/bin/python3
def best_score(a_dictionary):
    MaxVal = 0
    MaxKey = None
    if not a_dictionary:
        return (None)
    for Key, Value in a_dictionary.items():
        if Value > MaxVal:
            MaxVal = Value
            MaxKey = Key
    return MaxKey
