#!/usr/bin/python3
i = 0
while i < 10:
    j = i + 1
    while j < 10:
        if i == 8 and j == 9:
            print("{:d}{:d}".format(i, j))
            break
        if i < j:
            print("{:d}{:d}, ".format(i, j), end='')
        j = j + 1
    i = i + 1
