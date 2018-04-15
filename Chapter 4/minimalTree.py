from Node import Node
#creates a minimal tree from a sorted array
class minimalTree:
	def createBinTree(self,array):
		return self.addNode(array,0,len(array)-1)
	def addNode(self,array,front,back):
		if front > back: return
		mid = (front+back)/2
		root = Node(array[mid])
		root.left = self.addNode(array,front,mid-1)
		root.right = self.addNode(array,mid+1,back)
		return root

#testing
a = [1,2,3,4,8,22,34,38,54]
mT = minimalTree()
n = mT.createBinTree(a)
n.inOrder(n)