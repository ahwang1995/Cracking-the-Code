from Node import Node
#check if a tree is the subtree of another
class checkSubtree:
	#check if 2 subtrees are equal
	def checkEqual(self,T1,T2):
		if T1 == None and T2 == None: return True
		if T1 == None or T2 == None: return False
		return T1.data == T2.data and self.checkEqual(T1.left,T2.left) and self.checkEqual(T1.right,T2.right)

	#check each pair of nodes
	def checkST(self,T1,T2):
		#if t1 is smaller than t2, then it does not lie in that subtree
		if T2 == None: return True
		if T1 == None: return False

		if(self.checkEqual(T1,T2)): return True

		return self.checkST(T1.left,T2) or self.checkST(T1.right,T2)


#test
root = Node(5)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(3)

subNode = Node(2)
subNode.left = Node(1)
subNode.right = Node(3)

cst = checkSubtree()
print(cst.checkST(root,subNode))