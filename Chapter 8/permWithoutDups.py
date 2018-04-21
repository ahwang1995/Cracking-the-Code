#compute all permutations of a string of unique characters
class permWithoutDups:
	#recursive solution
	def Permute(self,string):
	    if len(string) == 0:
	        return ['']
	    prevList = self.Permute(string[1:len(string)])
	    nextList = []
	    for i in range(0,len(prevList)):
	        for j in range(0,len(string)):
	            newString = prevList[i][0:j]+string[0]+prevList[i][j:len(string)-1]
	            #dont think this if condition is needed, shouldnt have duplicate entries
	            if newString not in nextList:
	            	nextList.append(newString)
	    return nextList

pwd = permWithoutDups()
print pwd.Permute("abcd")