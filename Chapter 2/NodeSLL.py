class Node:

	#constructor
	def __init__(self,data=None,next=None):
		self.data = data
		self.next = next

	#add a node to the list
	def appendToTail(self,data):
		node = Node(data)
		n = self
		print("before")
		while(n.next != None):
			n = n.next
		print("after")
		n.next = node

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
#asdf = Node(3)
#asdf.appendToTail(2)