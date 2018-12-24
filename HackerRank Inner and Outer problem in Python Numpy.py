import numpy
n = numpy.array([input().split() for i in range(1)],int)
m = numpy.array([input().split() for i in range(1)],int)

print(int(numpy.inner(n,m)))
print(numpy.outer(n,m))
