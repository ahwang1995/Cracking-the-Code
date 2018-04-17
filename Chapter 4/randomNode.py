from Node import Node
import random
class randomNode:
	#visit each node and add it to an array
	def buildArr(self,node,arr):
		if node != None:
			arr.append(node)
			self.buildArr(node.left,arr)
			self.buildArr(node.right,arr)

	#pick a random node in the array
	def randNode(self,root):
		array = []
		self.buildArr(root,array)
		return array[random.randint(0,len(array)-1)]

n = Node(1)
n.left = Node(3)
n.right = Node(5)
n.left.left = Node(7)
n.left.right = Node(2)
n.right.left = Node(9)
n.right.right = Node(8)
r = randomNode()
print(r.randNode(n).data)
