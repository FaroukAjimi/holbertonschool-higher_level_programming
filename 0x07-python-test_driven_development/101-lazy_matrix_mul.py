#!/usr/bin/python3
import numpy
def lazy_matrix_mul(m_a, m_b):
    A = numpy.array(m_a)
    B = numpy.array(m_b)
    C = A.dot(B)
    return(C)
