import numpy
a = input()
my_array = numpy.array(list(map(int,a.split())))
print(numpy.reshape(my_array,(3,3)))
