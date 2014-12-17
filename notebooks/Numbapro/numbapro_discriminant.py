import math
from numbapro import vectorize
import numpy
import time

@vectorize(['float32(float32, float32, float32)'], target='cpu')
def discriminant_cpu(a, b, c):
    return math.sqrt(b**2 - 4*a*c)

@vectorize(['float32(float32, float32, float32)'], target='parallel')
def discriminant_mcpu(a, b, c):
    return math.sqrt(b**2 - 4*a*c)

@vectorize(['float32(float32, float32, float32)'], target='gpu')
def discriminant_gpu(a, b, c):
    return math.sqrt(b**2 - 4*a*c)

n = 256*1024*1024

a = numpy.array(numpy.random.sample(n), dtype='float32')
b = numpy.array(numpy.random.sample(n) + 10, dtype='float32')
c = numpy.array(numpy.random.sample(n), dtype='float32')

start_time = time.time()

print discriminant_cpu(a, b, c)

print "Time elapsed CPU: ", time.time() - start_time, "s"

start_time = time.time()

print discriminant_mcpu(a, b, c)

print "Time elapsed Multi CPU: ", time.time() - start_time, "s"

start_time = time.time()

print discriminant_gpu(a, b, c)

print "Time elapsed GPU: ", time.time() - start_time, "s"