#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    j = 0
    s = []
    try:
        for i in range(0, x):
            s.append(my_list[i])
            print('{}'.format(my_list[i]), end='')
        print()
        return(x)
    except:
        print()
        for i in (my_list):
            j = j + 1
        return(j)
