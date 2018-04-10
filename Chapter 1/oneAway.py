#check two strings are one or zero edits away
def oneAway(str1,str2):
	#make sure the lengths of the strings don't differ bby more than one
	diff = abs(len(str1) - len(str2))
	if diff > 1: return False
	list1 = list(str1)
	list2 = list(str2)
	diff2 = 0
	#remove matching characters from each list one at a time
	while(len(list1) > 0 & len(list2) > 0):
		for c in list1:
			if c in list2:
				list1.remove(c)
				list2.remove(c)
			#if the two list's differ by a length greater than one then return false
			if abs(len(list1)-len(list2)) > 1: return False
	return abs(len(list1)-len(list2)) < 2
print oneAway("a","ab")