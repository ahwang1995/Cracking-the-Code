from Node import Node
from Queue import Queue
from collections import deque
class listofDepths:
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
		depthList.append(dequeue.append(root))
		while(not q.isEmpty()):
			r = q.dequeue()
			if r.depth > currDepth:
				currDepth = currdepth + 1
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