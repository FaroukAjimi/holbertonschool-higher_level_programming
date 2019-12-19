#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    a = my_list
    z = len(my_list)
    for i in range(0, z):
        if idx == i:
            a[i] = element
            return (a)
        elif idx < 0:
            return (my_list)
        elif idx > z:
            return (my_list)
