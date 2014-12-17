from mpi4py import MPI

comm = MPI.COMM_WORLD
numproc = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

print "Hello World!! I am process %d of %d on %s." % (rank, numproc, name)
