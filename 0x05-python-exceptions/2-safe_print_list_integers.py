#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    i = 0
    for j in range(0, x):
        try:
            i = i+1
            print("{:d}".format(my_list[j]), end="")
        except (ValueError, TypeError):
            pass
    print()
    return(i)
