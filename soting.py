


a = [3,5,6,-1,0]

for  i in range(len(a)-1,0):
	max = 0
	for j in range(1,i+1):
		if a[j] > a[max]:
			max = j
	tmp =a[i]
	a[i] =a[max]
	a[max] = tmp
print a
		
			