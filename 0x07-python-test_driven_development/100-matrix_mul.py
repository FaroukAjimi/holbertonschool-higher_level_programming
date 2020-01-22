#!/usr/bin/python3
def matrix_mul(m_a, m_b):
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
    print(l)
    print(t)
