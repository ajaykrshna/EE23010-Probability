# Written by
# Ajay Krishnan K
# EE22BTECH11003

# Code for finding Area of triangle

import numpy as numpy

# Create the vectors
A = numpy.array([[1],[-1]])
B = numpy.array([[-4],[6]])
C = numpy.array([[-3],[-5]])

# Cross prod
# Arrays are flatten to take cross product
cross_prod = numpy.cross((A - B).flatten(), (A - C).flatten())

# Find the area
norm = numpy.linalg.norm(cross_prod)
area = 1/2 * norm
print("Area of triangle ABC : ", area, "sq units")