#!/usr/bin/python3
def magic_string(H = 'Holberton', i = 1):
    z = H + (' ,Holberton' * i)
    print(z)
    i = i + 1
    magic_string(H, i)
    return
