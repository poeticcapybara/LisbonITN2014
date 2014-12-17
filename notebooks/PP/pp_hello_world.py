import pp

def build_hello():
	return "h"+"e"+"l"+"l"+"o"

def build_world():
	return "w"+"o"+"r"+"l"+"d"


job_server = pp.Server()

print "Starting pp with", job_server.get_ncpus(), "workers."

job1 = job_server.submit(build_hello)
job2 = job_server.submit(build_world)

result1 = job1()
result2 = job2()

print result1 + " " + result2