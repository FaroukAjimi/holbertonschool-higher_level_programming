#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    b = 0
    for i in my_list:
        if i not in uniq:
            uniq.append(i)
    z = len(uniq)
    for i in range(z):
        b = b + uniq[i]
    return(b)
