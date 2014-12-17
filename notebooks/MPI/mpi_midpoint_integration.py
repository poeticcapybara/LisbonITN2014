from mpi4py import MPI
import numpy
import time

def func_val(x):
	# return pow(sin(x)+cos(x),1/3.0)
	# return sin(x)
	# return pow(x,3)+pow(x,2)+3*x+4;
	# return 2*pow(x,2)/ (3*pow(x,5)+4);
	return 4/(1+x*x) # should return Pi for int from 0 .. 1 = (4 * atan(1) )

def simpleint(a, m, h):
	result = 0
	# This is simple midpoint integration
	for x in range(0,m):
		result += func_val(a + x*h + h/2) # average function value between a and a+h
	return result * h                     # multiply with width=h to compute surface


comm = MPI.COMM_WORLD
numproc = comm.Get_size()
rank = comm.Get_rank()

a = 0
b = 1
m = 1000000

if (rank == 0):
	start_time = time.time()

result  = numpy.empty(1, dtype='d')
lresult = numpy.empty(1, dtype='d')

i = float(b-a)
h = i/m
lm = m/numproc
if(lm == 0):
	lm = 1
la = a + rank*i/numproc
lresult[0] = simpleint(la,lm,h)

comm.Reduce([lresult, MPI.DOUBLE], [result, MPI.DOUBLE], op=MPI.SUM, root = 0)

if (rank == 0):
	print "Integral of f between", (a,b), "is", result[0]
	print "Time elapsed: ", time.time() - start_time, "s"

