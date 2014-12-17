from numbapro import vectorize
import numpy
import time

@vectorize(['float32(float32, float32)'], target='gpu')
def sumarrays(a, b):
    return a + b

n = 16*1024*1024
a = numpy.arange(n, dtype='float32')
b = a*2

start_time = time.time()

sumarrays(a, b)

print "Time elapsed: ", time.time() - start_time, "s"