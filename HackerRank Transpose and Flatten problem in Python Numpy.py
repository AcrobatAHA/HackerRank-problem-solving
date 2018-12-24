import numpy
n,m = map(int,input().split())
my_array = numpy.array([input().split() for i in range(n)],int)
print(numpy.transpose(my_array))
print(my_array.flatten())
