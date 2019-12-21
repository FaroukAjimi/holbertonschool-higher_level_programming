#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = len(my_list)
    b = [i for i in my_list]
    for i in range(a):
        if b[i] == search:
            b[i] = replace
    return(b)
