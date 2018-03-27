def isUnique(stri):
	uChars = set()
	for c in stri:
		if c in uChars: return False
		uChars.add(c)
	return True
print isUnique("asfhi")