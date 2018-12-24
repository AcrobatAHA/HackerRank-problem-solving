import numpy
n,m = map(int,input().split())
my_array = numpy.array([input().split() for i in range(n)],int)
Min_number = numpy.min(my_array,axis = 1)
print(numpy.max(Min_number))
