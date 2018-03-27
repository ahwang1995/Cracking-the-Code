def oneAway(str1,str2):
	diff = abs(len(str1) - len(str2))
	if diff > 1: return False
	list1 = list(str1)
	list2 = list(str2)
	diff2 = 0
	while(len(list1) > 0 & len(list2) > 0):
		for c in list1:
			if c in list2:
				list1.remove(c)
				list2.remove(c)
			if abs(len(list1)-len(list2)) > 1: return False
	return abs(len(list1)-len(list2)) < 2
print oneAway("a","ab")