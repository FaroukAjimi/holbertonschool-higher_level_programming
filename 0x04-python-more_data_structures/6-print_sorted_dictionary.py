#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = {}
    for i, y in sorted(a_dictionary.items()):
        print("{} : {}".format(i, y))
