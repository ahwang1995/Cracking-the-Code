from Node import Node
class inOrder:
	def inOrderTraversal(node):
		if node != None:
			self.inOrderTraversal(node.left);
			print (node.data)
			self.inOrderTraversal(node.right)