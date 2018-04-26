from collections import Counter
#counts the characters in each string to check if it is an anagram
#and then sorts based on those values
class groupAnag:
	def groupA(self,arr):
		#get the counts
		countArr = [None]*len(arr)
		for i in range(0,len(arr)):
			countArr[i] = Counter(arr[i])
		#sort based on counts
		z = sorted(zip(countArr,arr), key = lambda count:count[0])
		#return the sorted string array
		return [string for count,string in z]

ga = groupAnag()
print ga.groupA(["asdf","ghjk","fdsa","kjhg"])