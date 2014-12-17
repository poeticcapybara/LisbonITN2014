from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
	data = {'a': 7, 'b': 3.14}
	comm.send(data, dest=1)
elif rank == 1:
	time.sleep(1)
	data = comm.recv(source=0)
else:
	data = None

print "I am process %d, received: " % rank, data
