import sys
import math
import time
import pp

def isprime(n):
	#Returns True if n is prime and False otherwise
	if not isinstance(n, int):
		raise TypeError("argument passed to is_prime is not of 'int' type")
	if n < 2:
		return False
	if n == 2:
		return True
	max = int(math.ceil(math.sqrt(n)))
	i = 2
	while i <= max:
		if n % i == 0:
			return False
		i += 1
	return True

def sum_primes(n1, n2):
	# Calculates sum of all primes between given integers n1 and n2
	if n1 >= n2:
	    print "Second argument has to be greater than the first one."
	    return 0
	return sum([x for x in xrange(n1, n2+1) if isprime(x)])


if len(sys.argv) > 1:
	ncpus = int(sys.argv[1])
	# Creates jobserver with ncpus workers
	job_server = pp.Server(ncpus)
else:
	# Creates jobserver with automatically detected number of workers
	job_server = pp.Server()
	ncpus = job_server.get_ncpus()

print "Starting pp with", ncpus, "workers"

n = 1000000

inputs = [( i*n/ncpus + 1, (i+1)*n/ncpus ) for i in range(0,ncpus)]

start_time = time.time()

jobs = [(input, job_server.submit(sum_primes, input, (isprime,), ("math",))) for input in inputs]

total_sum = 0
for input, job in jobs:
	print "Sum of primes between", input, "is", job()
	total_sum += job()

print "Total sum of primes until", n, "is", total_sum

print "Time elapsed: ", time.time() - start_time, "s"

job_server.print_stats()
