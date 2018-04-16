from Node import Node
from Queue import Queue
from collections import deque
from minimalTree import minimalTree
class listOfDepths:
	def __init__(self):
		self.depthList = []

	#use method similar to BFS to create array with linked lists of nodes in corresponding depths
	def makeList(self,root):
		q = Queue()
		root.visited = True
		root.depth = 0
		q.enqueue(root)
		#track the number of nodes visited so far
		currDepth = 0
		rootList = deque()
		rootList.append(root)
		self.depthList.append(rootList)
		while(not q.isEmpty()):
			r = q.dequeue()
			if r.depth > currDepth:
				currDepth = currDepth + 1
				nextList = deque()
				nextList.append(r)
				self.depthList.append(nextList)
			else:
				self.depthList[len(self.depthList)-1].append(r)

			#print(r.data)
			if r.left:
				r.left.depth = currDepth + 1
				q.enqueue(r.left)
			if r.right:
				r.right.depth = currDepth + 1
				q.enqueue(r.right)
		return self.depthList

#testing
a = [1,2,3,4,8,22,34,38,54]
mT = minimalTree()
n = mT.createBinTree(a)
#n.inOrder(n)
lod = listOfDepths()
depthLists = lod.makeList(n)
print depthLists[0][0].data
print depthLists[1][0].data
print depthLists[1][1].data
print depthLists[2][2].data
print depthLists[2][3].data