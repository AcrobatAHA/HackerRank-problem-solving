import numpy

n = int(input())
ls = numpy.array([input().split() for i in range(n)],float)
numpy.set_printoptions(legacy = '1.13')
print(numpy.linalg.det(ls))
