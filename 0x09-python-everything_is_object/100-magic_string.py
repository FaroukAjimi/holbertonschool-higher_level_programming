#!/usr/bin/python3
def magic_string(H = 'Holberton', i = 0):
    id(i)= 0
    z = H + (' ,Holberton' * i)
    i = i + 1
    return(z)
