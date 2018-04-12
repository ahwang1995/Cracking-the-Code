from NodeSLL import Node
#checks if there is a loop in the linked list
#if there is one return the node at the sstrt of the loop
def loopDetection(head):
	checked = list()
	n = head
	while(n.next != None):
		checked.append(n)
		if n.next in checked: return n.next
		n = n.next
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

"""headNode2 = headNode1
n = headNode1
for x in range(0,2):
	n = n.next
for x in range(0,5):
	headNode2 = headNode2.next
headNode2.next = n"""

print(loopDetection(headNode1))