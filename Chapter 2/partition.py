from NodeSLL import Node
#make it so that all notes less than x come before
#all nodes greater or equal to x
def partition(head,x):
	n = head
	#check to see if x is in the list, if it is, move it to the tail
	while(n.next != None):
		if (n.data == x):
			head.deleteNode(x)
			head.appendToTail(x)
		elif (n.next == None):
			return False
		n = n.next
	n = head
	while(n.next != None):
		print(n.data)
		n = n.next
	n = head

	#iterate through the list and each time a node smaller than x is found
	#move it to the head
	while(n.next != None):
		if(n.data < x):
			d = n.data
			n = n.next
			head.deleteNode(d)
			newNode = Node(d)
			head.prev = newNode
			newNode.next = head
			head = newNode
			continue
		n = n.next
	return head

headNode = Node(3)
headNode.appendToTail(7)
headNode.appendToTail(4)
headNode.appendToTail(2)
headNode.appendToTail(9)
headNode.appendToTail(6)
headNode.appendToTail(11)

headNode = partition(headNode,7)
n = headNode
while(n.next != None):
	#print(n.data)
	n = n.next

	
