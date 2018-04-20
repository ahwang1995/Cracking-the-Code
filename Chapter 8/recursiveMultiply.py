#multiply to integers using a recursive function
#and no multiply or divide operations
class recursiveMultiply:
	def mult(self,x,y):
		smaller = x
		greater = y
		if x > y:
			smaller = y
			greater = x
		return self.recMult(smaller,greater)

	def recMult(self,x,y):
		if x == 0:
			return 0
		elif x == 1:
			return y
		s = x >> 1
		half = self.recMult(s,y)
		if(x%2 == 0):
			return half + half
		else:
			return half + half + y

rm = recursiveMultiply()
print rm.mult(5,3)