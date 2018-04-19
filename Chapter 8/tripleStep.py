#count how many different ways a child can run up n stairs if they can
#either hop 1 2 or 3 stairs at a time
class tripleStep:
	def numWays(self,n):
		#table to store already calculated values during recursion
		table = [None for _ in xrange(n+1)]
		return self.countSteps(n,table)

	#recursive function to calculate number of ways to reach the top of
	#the stairs
	def countSteps(self,n,table):
		if n < 0:
			return 0
		elif n == 0:
			return 1
		else:
			table[n] = self.countSteps(n-1,table) + self.countSteps(n-2,table) + self.countSteps(n-3,table)
		return table[n]
#test
ts = tripleStep()
print ts.numWays(8)