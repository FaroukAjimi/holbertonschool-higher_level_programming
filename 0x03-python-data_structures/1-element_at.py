#!/usr/bin/python3
def element_at(my_list, idx):
    a = len(my_list)
    if idx < 0:
        return ("None")
    if idx > a:
        return ("None")
    for i in range(0, a):
        if i == idx:
            return (my_list[i])
        elif idx < 0:
            return ("None")
        elif idx > a:
            return ("None")
