
def retKthLast(head,k):
	n1 = head
	n2 = head
	counter = k
	while(counter!= 0):
		counter -= 1
		n1 = n1.next
	while(n1.next != None):
		n1 = n1.next
		n2 = n2.next
	return n2
