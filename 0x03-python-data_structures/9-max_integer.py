#!/usr/bin/python3
def max_integer(my_list=[]):
    l = len(my_list)
    if l == 0:
        return (None)
    maxi = my_list[0]
    for i in range(1, l):
        if my_list[i] > maxi:
            maxi = my_list[i]
    return (maxi)
