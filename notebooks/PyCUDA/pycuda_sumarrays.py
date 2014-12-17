import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import numpy
import time

C_cuda_code = SourceModule("""
__global__ void sum_arrays(float *a, float *b, float *c)
{
	const int i = blockIdx.x*blockDim.x + threadIdx.x;
	c[i] = a[i] + b[i];
}
""")

n = 16*1024*1024
a = numpy.random.randn(n).astype('f')
b = numpy.random.randn(n).astype('f')
c = numpy.zeros(n).astype('f')

a_gpu = cuda.mem_alloc(a.nbytes)
b_gpu = cuda.mem_alloc(b.nbytes)
c_gpu = cuda.mem_alloc(c.nbytes)

start_time = time.time()

cuda.memcpy_htod(a_gpu, a)
cuda.memcpy_htod(b_gpu, b)

func = C_cuda_code.get_function("sum_arrays")

size_block = 1024
size_grid = int((n-1)/size_block + 1)
func(a_gpu, b_gpu, c_gpu, block=(size_block,1,1), grid=(size_grid,1))

cuda.memcpy_dtoh(c, c_gpu)

print "Time elapsed GPU: ", time.time() - start_time, "s"

start_time = time.time()
c_cpu = a + b
print "Time elapsed CPU: ", time.time() - start_time, "s"

print numpy.alltrue(abs(c-c_cpu) < 1e-5)