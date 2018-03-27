class Node:

	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

	def appendToTail(self,data):
		node = Node(data)
		n = self
		while(n.next != None):
			n = n.next
		n.next = node
		node.prev = n

	def deleteNode(head,d):
		n = head
		if (n.data == d): return head.next

		while(n.next != None):
			if(n.next.data == d):
				n.next.next.prev = n
				n.next = n.next.next
				return head
			n = n.next
		return head
asdf = Node(3)
asdf.appendToTail(2)