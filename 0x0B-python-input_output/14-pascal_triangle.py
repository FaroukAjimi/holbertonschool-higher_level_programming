#!/usr/bin/python3
def pascal_triangle(n):
    """
    pascal_triangle
    function
    """
    triangle = []
    if n <= 0:
        return([])
    for i in range(n):
        triangle.append([])
    c = 0
    for i in range(len(triangle)):
        c += 1
        for x in range(c):
            triangle[i].append(1)
    for i in range(len(triangle)):
        for y in range(n):
            try:
                if (i-1) >= 0 and y-1 >= 0:
                    triangle[i][y] = triangle[i-1][y] + triangle[i - 1][y - 1]
            except IndexError:
                continue
    return(triangle)
