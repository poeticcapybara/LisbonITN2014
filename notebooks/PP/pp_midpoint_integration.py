import sys
import time
import pp

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


if len(sys.argv) > 1:
	ncpus = int(sys.argv[1])
	# Creates jobserver with ncpus workers
	job_server = pp.Server(ncpus)
else:
	# Creates jobserver with automatically detected number of workers
	job_server = pp.Server()
	ncpus = job_server.get_ncpus()

print "Starting pp with", ncpus, "workers"

a = 0
b = 1
m = 1000000

i = float(b - a)
h = i/m

start_time = time.time()

lm = m/ncpus
if(lm == 0):
	lm = 1
local_a = [( a + j*i/ncpus) for j in range(0,ncpus)]

jobs = [job_server.submit(simpleint, (la,lm,h), (func_val,)) for la in local_a]

total_sum = 0
for job in jobs:
	total_sum += job()

print "Integral of f between", (a,b), "is", total_sum

print "Time elapsed: ", time.time() - start_time, "s"

job_server.print_stats()