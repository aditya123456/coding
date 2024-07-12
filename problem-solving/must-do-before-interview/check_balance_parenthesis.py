s1= ')()(())))'
s2='(()(()('


s3='(((()))))'
s4='(()'



def check_balance(str1, str2):
	s = str1+str2
	stack = list(s)
	stack2=[]
	for i in stack:
		if i =='(':
			stack2.append(i)
		else:
			if stack2 ==[]:
				print ("blanced")
				return False
			else:
				stack2.pop()
	print (stack2)
	if not stack2==[]:
		print ("not blanced")
		return False
	return True
			
			
			
print(check_balance(s2,s1))
print (check_balance(s3,s4))
