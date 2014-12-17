import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import numpy
import time

C_cuda_code = SourceModule("""
__global__ void MC_Pi(float *U1, float *U2, float *counter)
{
	const int i = blockIdx.x*blockDim.x + threadIdx.x;
	counter[i] = 0;
	if( (pow(U1[i],2) + pow(U2[i],2)) <= 1.0 )
			counter[i] = 1;
}
""")

n = 16*1024*1204
U1 = numpy.random.rand(n).astype('f')
U2 = numpy.random.rand(n).astype('f')
counter = numpy.zeros(n).astype('f')

start_time = time.time()


func = C_cuda_code.get_function("MC_Pi")

size_block = 1024
size_grid = int((n-1)/size_block + 1)
func(cuda.In(U1), cuda.In(U2), cuda.Out(counter), block=(size_block,1,1), grid=(size_grid,1))

counter = numpy.sum(counter)

print "PI_gpu = ", 4.0*counter/n
print "Time elapsed GPU: ", time.time() - start_time, "s"

start_time = time.time()

counter_cpu = numpy.sum( (numpy.power(U1,2) + numpy.power(U2,2)) <= 1.0 )

print "PI_cpu = ", 4.0*counter_cpu/n
print "Time elapsed CPU: ", time.time() - start_time, "s"
