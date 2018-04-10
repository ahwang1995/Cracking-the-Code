#checks if a string has only unique characters
def isUnique(stri):
	uChars = set()
	#iterate through the string, if character has not already been found then add it to checked list
	for c in stri:
		if c in uChars: return False
		uChars.add(c)
	return True
print isUnique("asfhi")