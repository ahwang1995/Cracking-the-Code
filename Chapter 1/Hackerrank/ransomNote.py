from collections import Counter
def ransom_note(magazine, ransom):
    count_a = Counter(magazine)
    count_b = Counter(ransom)
    for i in count_b.keys():
    	if count_a[i] - count_b[i] < 0: return False
    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if((m-n) < 0): print "No"
else:
	if(answer):
		print "Yes"
	else:
		print "No"
    
