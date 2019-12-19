#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = len(my_list)
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    r = []
    for i in range(0, a):
        r.append(my_list[i])
    r[idx] = element
    return (r)
