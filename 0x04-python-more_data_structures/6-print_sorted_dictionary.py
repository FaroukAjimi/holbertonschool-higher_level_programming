#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = {}
    for i in a_dictionary:
        a[i] = a_dictionary[i]
    for i, y in sorted(a.items()):
        print("{}: {}".format(i, y))
