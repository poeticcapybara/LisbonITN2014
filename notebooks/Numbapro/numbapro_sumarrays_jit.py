from numbapro import cuda, float32, void
import numpy
import time

@cuda.jit(void(float32[:], float32[:], float32[:]))
def sumarrays(a, b, c):
	
	i = cuda.grid(1) # Short for cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
	
	if i < c.size:
		c[i] = a[i] + b[i]

n = 16*1024*1024
a = numpy.arange(n, dtype='float32')
b = a*2

start_time = time.time()

da = cuda.to_device(a)
db = cuda.to_device(b)
dc = cuda.device_array_like(a)

size_block = 1024
size_grid = int((n-1)/size_block + 1)
sumarrays[size_grid, size_block](da, db, dc)

c = dc.copy_to_host()

print "Time elapsed: ", time.time() - start_time, "s"
