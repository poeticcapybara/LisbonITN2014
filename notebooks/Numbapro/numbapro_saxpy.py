from numbapro import cuda, vectorize, float32, void
import numpy
import time

@cuda.jit(void(float32, float32[:], float32[:], float32[:]))
def saxpy(a, x, y, out):
	
	i = cuda.grid(1) # Short for cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
	
	if i < out.size:
		out[i] = a*x[i] + y[i]


@vectorize([float32(float32, float32, float32)], target='gpu')
def vec_saxpy(a, x, y):
	return a*x + y


n = 16*1024*1024

a = numpy.float32(2.0)
x = numpy.arange(n, dtype='float32')
y = numpy.arange(n, dtype='float32')
out = numpy.empty_like(x)

start_time = time.time()

size_block = 1024
size_grid = int((n-1)/size_block + 1)
saxpy[size_grid, size_block](a, x, y, out)

print "Time elapsed JIT: ", time.time() - start_time, "s"

start_time = time.time()

a = a*numpy.ones(n, dtype='float32')
vecout = vec_saxpy(a, x, y)

print "Time elapsed VEC: ", time.time() - start_time, "s"

print "Correct result? ", numpy.alltrue(abs(out-vecout) < 1e-5)
