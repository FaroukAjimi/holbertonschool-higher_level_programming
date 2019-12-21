#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = len(my_list)
    b = [i for i in my_list]
    for i in range(0, search):
        b[search - 1] = replace
    return(b)
