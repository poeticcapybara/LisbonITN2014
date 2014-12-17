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


a = 0
b = 1
m = 1000000

i = float(b - a)
h = i/m

start_time = time.time()

print "Integral of f between", (a,b), "is", simpleint(a, m, h)

print "Time elapsed: ", time.time() - start_time, "s"