#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = len(my_list)
    b = [i for i in my_list]
    b.insert(search, replace)
    b.remove(search)
    return(b)
