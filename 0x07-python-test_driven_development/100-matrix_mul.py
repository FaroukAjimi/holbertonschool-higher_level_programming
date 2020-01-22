#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not(isinstance(m_a, list)):
        raise TypeError('m_a must be a list')
    if not(isinstance(m_b, list)):
        raise TypeError('m_b must be a list')
    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')
    p = 0
    for i in range(len(m_a)):
        if p != 0:
            if (len(m_a[i]) != p):
                raise TypeError('each row of m_a must be of the same size')
            p = 0
        p = len(m_a[i])
        for y in range(len(m_a[i])):
            if not(isinstance (m_a[i][y], int)):
                raise TypeError('m_a should contain only integers or floats')
    p = 0
    for i in range(len(m_b)):
        if p != 0:
            if (len(m_b[i]) != p):
                raise TypeError('each row of m_a must be of the same size')
            p = 0
        p = len(m_b[i])
        for y in range(len(m_b[i])):
            if not(isinstance(m_b[i][y], int)):
                raise TypeError('m_b should contain only integers or floats')
    c = 0
    if len(m_a) < len(m_b):
        c = m_b
        b = m_a
    elif len(m_a) >= len(m_b):
        c = m_a
        b = m_b
    l = []
    t = []
    for i in b:
        t.append([])
    for i in c:
        l.append([])
    for i in range(len(m_b)):
        for y in range(len(m_b)):
            try:
                l[i].append(m_b[y][i])
            except:
                l[i].append(0)
    i = 0
    y = 0
    a = 0
    for i in range(len(m_a)):
        for z in range(len(l)):
            for y in range(len(m_a[0])):
                if a != 0:
                    a += m_a[i][y]*l[z][y]
                    t[i].append(a)
                    a = 0
                    continue
                a = m_a[i][y]*l[z][y]
    return(t)
