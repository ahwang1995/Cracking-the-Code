from collections import Counter
def isPalinPerm(stri):
	count = Counter(stri)
	countval = count.values()
	numodd = 0
	for c in countval:
		if c%2 == 1: numodd += 1
		if numodd > 1: return False
	return True

print isPalinPerm("asfsfja")