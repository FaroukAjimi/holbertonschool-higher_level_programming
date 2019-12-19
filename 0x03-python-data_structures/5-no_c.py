#!/usr/bin/env python3
def no_c(my_string):
    sp = ''
    for i in my_string:
        if i == 'C' or i == 'c':
            i = ''
        sp += i
    return (sp)
