#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return(0)
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    a = 0
    s = list(roman_string)
    for i, y in r.items():
        for k in s:
            if i == k:
                a = a + y
    return(a)
