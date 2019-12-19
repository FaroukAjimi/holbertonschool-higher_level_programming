#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    z = len(my_list)
    for i in range(0, z):
        if idx == i:
            my_list[i] = element
            return (my_list)
        elif idx < 0:
            return (my_list)
        elif idx > z - 1:
            return (my_list)
