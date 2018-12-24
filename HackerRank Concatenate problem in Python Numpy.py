import numpy
n,m,p = map(int,input().split())
my_array = numpy.array([input().split() for i in range(n+m)],int)
print(my_array)
