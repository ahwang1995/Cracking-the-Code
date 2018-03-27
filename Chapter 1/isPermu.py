def isPermu(str1,str2):
	pChar = list(str1)
	for c in str2:
		if c not in pChar: return False
		pChar.remove(c)
	return True
print isPermu("asdf","fdsaq")
