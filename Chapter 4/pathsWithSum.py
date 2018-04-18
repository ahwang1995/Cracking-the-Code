from Node import Node
class pathsWithSum:
	def __init__(self):
		self.count = 0
	#count the number of paths in a tree that sum up to a given value
	#the path does not have to start at the root or end at a leaf
	def pathSum(self,root,total):
		self.countPaths(root,0,total)
		if(root != None):
			self.pathSum(root.left,total)
			self.pathSum(root.right,total)
		return self.count

	#do a preorder traversal on every node to get the number of paths
	#this solution is N^2, may be able to make a better solution
	def countPaths(self,node,currTotal,total):
		if node != None:      
			if (currTotal + node.data == total):
				self.count = self.count + 1 
			self.countPaths(node.left,currTotal+node.data,total)
			self.countPaths(node.left,currTotal+node.data,total)
#test
n = Node(1)
n.left = Node(2)
n.left.left = Node(3)
n.left.right = Node(6)
n.right = Node(3)
n.left.left = Node(2)
n.left.right = Node(6)

ps = pathsWithSum()
print (ps.pathSum(n,6))
