from Node import Node
#find the first common ancestors of 2 nodes in a binary tree
class firstCommonAncestor:
	def FCA(self,root,node1,node2):
		if root == None:
			return None

		#if node is found return the node
		if root.data == node1.data or root.data == node2.data:
			return root

		#check if the node is in the left or right subtree
		leftTree = self.FCA(root.left,node1,node2)
		rightTree = self.FCA(root.right,node1,node2)

		#if both are true, then the ancestor node is the root
		if leftTree and rightTree:
			return root

		#if both the keys are in the left tree then the ancestor is in the left
		if leftTree is not None: return leftTree
		else: return rightTree

#test
root = Node(5)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(3)
fca = firstCommonAncestor()
print(fca.FCA(root,root.left.left,root.left.right).data)