from NodeSLL import Node
#remove duplicate nodes in a linked list
def removeDups(head):
	visited = list()
	n = head
	while(n.next != None):
		visited.append(n.data)
		if n.next.data in visited:
			n.next = n.next.next
			n.next.prev = n
		n = n.next
	return head
a = Node(3)