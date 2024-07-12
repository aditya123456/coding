
class sorting:
	def __init__(self, list1):
		self.l = list1
	def test_buble_sort(self):
		for i in range(len(self.l)):
			for j in range(i+1,len(self.l)):
				if self.l[i]>self.l[j]:
					tmp = self.l[i]
					self.l[i]=self.l[j]
					self.l[j] = tmp
		return self.l

		
	def selection_sort(self):
		for i in range(len(self.l)-1,0):
			max = 0
			for j in range(1,i+1):
				if self.l[j] > self.l[max]:
					max = j
			tmp =self.l[i]
			self.l[i] =self.l[max]
			self.l[max] = tmp
		return self.l
		
	# def binary_search(self, element):
	# 	l = 0
	# 	r = len(self.list1)-1
	#
	# 	while r<=l:
	# 		mid = (l)+r)/2
	# 		if self.list1[mid] == element:
	# 			return True
	# 		elif self.list1[mid]<element:
	# 			r = mid +1
	# 		else:
	# 			l = mid -1
	# 	return False
		
		
list1 = [3,-4,5,6,7,-1,2,0,-9]
s = sorting(list1)

print(s.test_buble_sort())
print(s.selection_sort())