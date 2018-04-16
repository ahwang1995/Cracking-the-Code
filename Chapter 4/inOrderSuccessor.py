from Node import Node
#find the inorder successor of a given node in a binary search tree
class inOrderSuccessor:
	def getSuccessor(self,node,root):
		#if there is a right node then the node is in that subtree
		if node.right != None:
			succNode = node.right
			self.getMin(node.right,node.right.data,succNode)
			return succNode
		succNode = None
		#if there is no right node then iterate through the tree starting from the root
		while(root != None):
			if(node.data < root.data):
				succNode = root
				root = root.left
			elif node.data > root.data:
				root = root.right
			else: break
		return succNode

	#get the min value in the right subtree
	def getMin(self,node,minVal,succNode):
		if node.right != None:
			if node.right.data < minVal:
				succNode = node.right
				minVal = node.right.data
			self.getMin(node.right,minVal,succNode)
		if node.left != None:
			if node.left.data < minVal:
				succNode = node.left
				minVal = node.left.data
			self.getMin(node.left,node.left)
		return minVal,succNode

#testing
root = Node(5)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(3)
ios = inOrderSuccessor()
print(ios.getSuccessor(root.left,root)).data