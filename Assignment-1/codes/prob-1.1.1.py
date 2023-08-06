import numpy as numpy

vector_a = numpy.array([[1],[-1]])
vector_b = numpy.array([[-4],[6]])
vector_c = numpy.array([[-3],[-5]])

dir_ab = vector_b - vector_a
dir_bc = vector_c - vector_b
dir_ca = vector_a - vector_c

print('direction vector of AB is \n', dir_ab)
print('direction vector of BC is \n', dir_bc)
print('direction vector of CA is \n', dir_ca)
