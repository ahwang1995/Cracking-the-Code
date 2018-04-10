from NodeSLL import Node
#delete a node in the linked list that is not the head or tail
def deleteMid(node):
	n = node.next
	node.data = n.data
	node.next.next.prev = node
	node.next = n.next
	return True
