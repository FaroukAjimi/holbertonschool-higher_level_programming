#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = {}
    for keys in a_dictionary:
        a[keys] = a_dictionary[keys] * 2
    return(a)
