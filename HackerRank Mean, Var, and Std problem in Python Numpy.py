import numpy

n,m = map(int,input().split())

val = numpy.array([input().split() for i in range (n)],int)
numpy.set_printoptions(legacy = '1.13')
print(numpy.mean(val,axis = 1))
print(numpy.var(val,axis = 0))
print(numpy.std(val,axis = None))
