#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = []
    for i in set_1:
        if i not in set_2:
            diff.append(i)
    for y in set_2:
        if y not in set_1:
            diff.append(y)
    return(diff)
