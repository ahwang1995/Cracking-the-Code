#use recursion and the fact that making change for larger values is equal
#one of the previous values calculated
class coins:
	def numWays(self,n):
		#the coin values used
		coinVals = {25,10,5,1}
		#number of ways for each value so far
		prevSums = [n+1][len(coinVals)]
		return self.calcWays(n,coinVals,0,prevSums)

	def calcWays(self,val,coinVals,ind,prevSums):
		#get a previously calculated value
		if prevSums[val][ind] > 0:
			return prevSums[val][ind]
		#if all the types of coins have been calculated return
		if ind >= len(coinVals)-1: return 1
		coinVal = coinVals[ind]
		ways = 0
		i = 0
		#recursion
		while(i*coinVal <= val):
			amountRem = val-i*coinVal
			ways = ways + self.calcWays(amountRem,coinVals,ind + 1,prevSums)
			i = i + 1
		prevSums[val][ind] = ways
		return ways

