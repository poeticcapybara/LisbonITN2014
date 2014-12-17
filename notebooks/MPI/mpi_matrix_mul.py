from mpi4py import MPI
import numpy
import time


comm = MPI.COMM_WORLD
numproc = comm.size
rank = comm.rank    

# Dimensions of the 1st matrix 'a'
x = 5096
y = 5096

if rank == 0:
	# two matrices to multiply
	a = numpy.random.uniform(size=(x,y)).astype('d')
	b = numpy.random.uniform(size=(y,x)).astype('d')
else:
	a = None
	b = numpy.zeros((y,x),dtype='d')

sub_x = x/numproc

# scatter destination
sub_a = numpy.zeros((sub_x,y),dtype='d')

# gather destination
c = numpy.zeros((x,x),dtype='d')

t1 = time.time()

# broadcast 2nd matrix 'b'
comm.Bcast([b,MPI.DOUBLE], root=0)

comm.Scatter([a,MPI.DOUBLE],[sub_a,MPI.DOUBLE], root=0)

sub_c = numpy.dot(sub_a,b)    

comm.Gather([sub_c,MPI.DOUBLE],[c,MPI.DOUBLE], root=0)

t2 = time.time()-t1
if rank==0:
	print "MPI matmul on %d CPUS (s)" % numproc, t2

if rank==0:
	t1 = time.time()
	single_c = numpy.dot(a,b)
	print "1 CPU (s)", time.time()-t1
	
	print numpy.alltrue(abs(c-single_c) < 1e-5)

