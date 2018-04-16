from Node import Node
class checkBalanced:
	#checks the heights of 2 subtrees of any node and
	#makes sure it doesn't differ by more than one
	def checkB(self,node):
		#if tree is empty then it is balanced
		if (node == None): return True
		left = self.getHeight(node.left)
		right = self.getHeight (node.right)

		if abs(left-right) <= 1 and self.checkB(node.left) and self.checkB(node.right):
			return True
		return False

	#get the height of a subtree
	def getHeight(self,node):
		if (node == None): return 0
		return 1 + max(self.getHeight(node.left),self.getHeight(node.right))

#Test
root = Node(4)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(1)
root.left.left.left = Node(4)
checkBal = checkBalanced()
print(checkBal.checkB(root))
