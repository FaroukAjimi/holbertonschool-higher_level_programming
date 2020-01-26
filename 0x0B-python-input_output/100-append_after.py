#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    l = []
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            count += 1
            for part in line.split():
                if search_string in part:
                    l.append(count)
    augment = 0
    for i in range(len(l)):
        l[i] = l[i] + augment
        augment += 1
    contents = None

    with open(filename, 'r') as file:
        contents = file.readlines()

    for index in range(len(l)):
        contents.insert(l[index], new_string)

    with open(filename, 'w') as file:
        contents = "".join(contents)
        file.write(contents)
