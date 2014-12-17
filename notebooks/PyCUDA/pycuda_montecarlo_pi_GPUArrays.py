import pycuda.driver as cuda
import pycuda.autoinit
import numpy
import time

import pycuda.gpuarray as gpuarray
import pycuda.curandom as curandom


n = 16*1024*1204
U1 = curandom.rand(n)
U2 = curandom.rand(n)
counter = gpuarray.zeros(n, dtype='f')

start_time = time.time()

counter = gpuarray.sum( (U1*U1 + U2*U2) <= 1.0 )

print "PI_gpu = ", 4.0*counter/n
print "Time elapsed GPUArrays: ", time.time() - start_time, "s"

# Sequential part

U1 = numpy.random.rand(n).astype('f')
U2 = numpy.random.rand(n).astype('f')

start_time = time.time()

counter_cpu = numpy.sum( (numpy.power(U1,2) + numpy.power(U2,2)) <= 1.0 )

print "PI_cpu = ", 4.0*counter_cpu/n
print "Time elapsed CPU: ", time.time() - start_time, "s"