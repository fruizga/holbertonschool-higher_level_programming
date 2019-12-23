#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        mult = sum([x * y for x, y in my_list])
        divi = sum(y for x, y in my_list)
        return (mult/divi)
