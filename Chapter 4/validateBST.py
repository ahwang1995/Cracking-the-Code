from Node import Node

#an alternative way to implement this is with an inorder traversal
#to implement with inorder traversal make sure that each node visited
#is greater than the one before it, if it is smaller then it is not a bst
class validateBST:
	#checks if a binary tree is a binary search tree
	def validBST(self,node):
		return self.checkSubtree(node,-99999,99999)

	#recursive tree that keeps track of the minimum and maximum values
	def checkSubtree(self,node,minVal,maxVal):
		if (node == None): return True
		if node.data > maxVal or node.data < minVal: return False
		return self.checkSubtree(node.left,minVal,node.data) and self.checkSubtree(node.right,node.data,maxVal)

#Test
root = Node(5)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(3)
valBST = validateBST()
print(valBST.validBST(root))
