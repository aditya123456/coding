
import time
n = 5
l = range(100000)
maxprod = 0
def slow_prod():
	
	stime = time.time()
	for i in l:
		prod = n*i
		if prod > maxprod:
			maxprod = prod
	e_time = time.time()
	ttime = e_time - stime
	print ttime
			
	print i
	print maxprod

	
def fast_prod():
	index =1
	for i in range(1,len(l)):
		if l[i]>l[index]:
			index = i
	index1=1
	for i in range(1,len(l)):
		if index != i and l[i]>l[index1]:
			index1 = i
	print l[index]
	print l[index1]
	print l[index]*l[index1]

	
def stress_test():
	import random
	while True:
		n = random.randint(1,101)
		l = range(n)
		index =1
		for i in range(1,len(l)):
			if l[i]>l[index]:
				index = i
		index1=1
		for i in range(1,len(l)):
			if index != i and l[i]>l[index1]:
				index1 = i
		print l[index]
		print l[index1]
		print l[index]*l[index1]

#fast_prod()
stress_test()