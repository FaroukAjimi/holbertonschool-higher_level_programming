#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename) as file:
        if nb_lines > 0:
            for i in range(nb_lines):
                print(next(file), end='')
        else:
            print(file.read(), end="")
