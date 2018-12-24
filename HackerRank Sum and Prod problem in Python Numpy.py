import numpy
n,m = map(int,input().split())
Lis= numpy.array([input().split() for i in range(n)],int)
Lis_Sum = numpy.sum(Lis,axis =0)
print(numpy.prod(Lis_Sum))
