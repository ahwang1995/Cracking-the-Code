from collections import Counter
def compStr(stri):
	count = Counter(stri)
	if(2*len(count) > sum(count.values())): return False
	cStr = ""
	for c in count:
		cStr += c + str(count[c])
	return cStr
print compStr("abbbbbbbbb")