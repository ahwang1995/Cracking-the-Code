from collections import Counter
def number_needed(a, b):
	count_a = Counter(a)
	count_b = Counter(b)
	count_a.subtract(count_b)
	return sum(abs(i) for i in count_a.values())

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
