import sys
print sys.version
def is_matched(expression):
	explen = len(expression)
	halflen = explen/2
	if explen%2 != 0: return False
	a = expression[:halflen]
	b = expression[halflen:explen]
	for i in range (0,halflen):
		if a[i] == '(' and b[halflen-1-i] != ')': return False
		elif a[i] == '[' and b[halflen-1-i] != ']': return False
		elif a[i] == '{' and b[halflen-1-i] != '}': return False
	return True

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"