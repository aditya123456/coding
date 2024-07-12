


def fibonicci(n):
	#while n>=0:
	if n<=1:
		print n
		return n
	
	print fibonicci(n-1)+fibonicci(n-2)
	return fibonicci(n-1)+fibonicci(n-2)
		#n=n-1

def fiblist(n):
		fblist = range(n)
		fblist[0]=0
		fblist[1]=1
		for i in range(2,len(fblist)):
			fblist[i] = fblist[i-1]+fblist[i-2]
		print fblist
		
		
		
#print fibonicci(14)
fiblist(10000)