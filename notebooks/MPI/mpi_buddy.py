from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
numproc = comm.Get_size()

data = None

if rank != numproc - 1:
	comm.send(rank, dest = rank + 1)

if rank != 0:
	data = comm.recv(source = rank - 1)

time.sleep(rank)

print "I am process %d, recived: " % rank, data