class Node:

	#constructor
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

	#add a node to the list (implemented as a doubly linked list)
	def appendToTail(self,data):
		node = Node(data)
		n = self
		while(n.next != None):
			n = n.next
		n.next = node
		node.prev = n

	#delete a node from the list
	def deleteNode(self,d):
		h = self
		n = self
		if (n.data == d): return h.next

		while(n.next != None):
			if(n.next.data == d):
				n.next.next.prev = n
				n.next = n.next.next
				return h
			n = n.next
		return h
asdf = Node(3)
asdf.appendToTail(2)