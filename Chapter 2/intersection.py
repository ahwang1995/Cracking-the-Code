from NodeSLL import Node
#if a node in one list is by reference, not by value a node
#in the other list then return True, else return false
def intersection(head1,head2):
	if head1.listLength() <= head2.listLength():
		while(head2.next != None):
			if head1 is head2: return True
			head2 = head2.next
	else:
		while(head1.next != None):
			if head1 is head2: return True
			head1 = head1.next
	if head1 is head2: return True
	return False

#Testing
headNode1 = Node(3)
headNode1.appendToTail(7)
headNode1.appendToTail(4)
headNode1.appendToTail(2)
headNode1.appendToTail(9)
headNode1.appendToTail(6)
headNode1.appendToTail(11)
headNode1.appendToTail(1)

#headNode2 = Node(6)
#headNode2.appendToTail(11)
#headNode2.appendToTail(1)
headNode2 = headNode1
for x in range(0,3):
	headNode2 = headNode2.next
print(intersection(headNode1,headNode2))