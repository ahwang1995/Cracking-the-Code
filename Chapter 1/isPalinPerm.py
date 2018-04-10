from collections import Counter
#check if a palindrome can be built from the characters in the string
def isPalinPerm(stri):
	#count the number of times each character occurs
	count = Counter(stri)
	countval = count.values()
	numodd = 0
	#make sure there is zero or one odd counts of characters in the string
	for c in countval:
		if c%2 == 1: numodd += 1
		if numodd > 1: return False
	return True

print isPalinPerm("asfsfja")