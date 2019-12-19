#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    z = my_list
    for i in range(1, 5):
        print('{:d}'.format(z[-i]))
    print('{:d}'.format(z[0]))
