import sys
import math
import time
import pp

def isprime(n):
	# Returns True if n is prime and False otherwise
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

def sum_primes(n):
	# Calculates sum of all primes until given integer n
	return sum([x for x in xrange(2,n+1) if isprime(x)])



if len(sys.argv) > 1:
	ncpus = int(sys.argv[1])
	# Creates jobserver with ncpus workers
	job_server = pp.Server(ncpus)
else:
	# Creates jobserver with automatically detected number of workers
	job_server = pp.Server()

print "Starting pp with", job_server.get_ncpus(), "workers"

# The following submits 8 jobs and then retrieves the results
inputs = (1000, 1001, 1002, 1003, 1004, 1005, 1006, 100700)

start_time = time.time()

jobn = pp.Template(job_server, sum_primes, (isprime,), ("math",))

jobs = [(input, jobn.submit(input)) for input in inputs]
for input, job in jobs:
	print "Sum of primes until", input, "is", job()

print "Time elapsed: ", time.time() - start_time, "s"

job_server.print_stats()