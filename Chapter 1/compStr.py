from collections import Counter
#compress a string to show it's character counts, if doing so reduces the length of the string
def compStr(stri):
	count = Counter(stri)
	if(2*len(count) > sum(count.values())): return False
	cStr = ""
	for c in count:
		cStr += c + str(count[c])
	return cStr
print compStr("abbbbbbbbb")