from NodeSLL import Node

def deleteMid(node):
	n = node.next
	node.data = n.data
	node.next.next.prev = node
	node.next = n.next
	return True
