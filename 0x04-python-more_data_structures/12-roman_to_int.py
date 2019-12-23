#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    roman_char = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    roman = [1, 5, 10, 50, 100, 500, 1000]
    romanSum = 0
    temp = 0
    letter = ''
    for i in range(len(roman_string)):
        letter = roman_string[i]
        for j in range(len(roman_char)):
            if letter == roman_char[j]:
                romanSum += roman[j]
                if temp < roman[j]:
                    romanSum -= temp * 2
                    temp = roman[j]
                else:
                    temp = roman[j]
    return romanSum
