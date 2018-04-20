#returns all subsets of a set in O(n2^n) time, this set is not ordered but satisifies req
class powerSet:
	#use the previous set to construct the next set
	def getSubset(self,initialSet,newSet):
		#base case
		if initialSet == []:
			return [newSet]
		#recursion, given 2 possibilities
		else:
			ret = []
			for x in self.getSubset(initialSet[1:],newSet+[initialSet[0]]):
				ret.append(x)
			for x in self.getSubset(initialSet[1:],newSet):
				ret.append(x)
			return ret
ps = powerSet()
print (ps.getSubset([1,2,3],[]))
print sorted(ps.getSubset([1,2,3],[]))
