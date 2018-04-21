class permWithDups:
	#recursive solution pretty much the same as without dups
	#TODO:make some cases terminate early so every possibility doesn't have to be checked
	def Permute(self,string):
	    if len(string) == 0:
	        return ['']
	    prevList = self.Permute(string[1:len(string)])
	    nextList = []
	    for i in range(0,len(prevList)):
	        for j in range(0,len(string)):
	            newString = prevList[i][0:j]+string[0]+prevList[i][j:len(string)-1]
	            #to prevent duplicate entries
	            if newString not in nextList:
	            	nextList.append(newString)
	    return nextList

pwd = permWithDups()
print pwd.Permute("abcda")