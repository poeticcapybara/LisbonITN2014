import math
import random
import time

def MC_Pi(n):
	counter = 0
	for i in range(n):
		if math.pow(random.random(), 2.0) + math.pow(random.random(), 2.0) <= 1.0:
			counter += 1
	return counter
        
n = 1000000
start_time = time.time()

ctr = MC_Pi(n)

print "PI = ", 4.0*ctr/n

print "Time elapsed: ", time.time() - start_time, "s"