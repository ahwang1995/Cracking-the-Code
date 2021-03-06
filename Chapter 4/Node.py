class Node:
	def __init__(self,data=None):
		self.data = data
		self.left = None
		self.right = None
		self.depth = None
	#implement inorder
	def inOrder(self,node):
		if node != None:
			self.inOrder(node.left)
			print (node.data)
			self.inOrder(node.right)

	#implement preorder
	def preOrder(self,node):
		if(node != None):
			print(node.data)
			self.preOrder(node.left)
			self.preOrder(node.right)

	#implement postorder
	def postOrder(self,node):
		if(node != None):
			self.postOrder(node.left)
			self.postOrder(node.right)
			print(node.data)