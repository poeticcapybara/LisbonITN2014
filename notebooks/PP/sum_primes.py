import math
import time

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

def sum_primes(n):
	#Calculates sum of all primes until given integer n
	return sum([x for x in xrange(2,n+1) if isprime(x)])


n = 1000000

start_time = time.time()

result = sum_primes(n)
print "Sum of primes until", n, "is", result

print "Time elapsed: ", time.time() - start_time, "s"