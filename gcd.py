

def slow_gcd(a, b):
	gcd = 0
	for d in range(1, (a+b)):
		print d
		if a/d and b/d:
			gcd =d
	return gcd
	
	
def fast_gcd(a, b):
	if b==0:
		return a
	a_ = a%b
	return fast_gcd(b, a_)
	
	
print slow_gcd(4,8)
print fast_gcd(100,200)