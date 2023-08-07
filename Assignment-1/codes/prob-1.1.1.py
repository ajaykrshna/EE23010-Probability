import numpy as numpy

A = numpy.array([[1],[-1]])
B = numpy.array([[-4],[6]])
C = numpy.array([[-3],[-5]])

AB = B - A
BC = C - B
CA = A - C

print('direction vector of AB is \n', AB)
print('direction vector of BC is \n', BC)
print('direction vector of CA is \n', CA)
