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

	#iterative solution (muuuuch easier)
	def getSubsetIter(self,initialSet):
		ret = [[]]
		for x in initialSet:
			newSets = [subset + [x] for subset in ret]
			ret.extend(newSets)
		return ret

ps = powerSet()
print (ps.getSubsetIter([1,2,3]))
