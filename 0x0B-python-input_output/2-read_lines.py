#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r') as file:
        if nb_lines > 0:
            for i in range(nb_lines):
                print(f.readlines(), end='')
        else:
            print(file.read(), end="")
