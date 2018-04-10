#check if one string is a permutation of the other
def isPermu(str1,str2):
	pChar = list(str1)
	#iterate through string 2 and remove elements after checking if the character
	#is in string 1
	for c in str2:
		if c not in pChar: return False
		pChar.remove(c)
	return True
print isPermu("asdf","fdsaq")
