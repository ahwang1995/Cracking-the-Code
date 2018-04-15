
from Queue import Queue
import copy
class Node:
	def __init__(self,data=None):
		self.data = data
		self.children = []
		self.visited = False

	def DFS(self,root):
		if (root == None): return
		print (root.data)
		root.visited = True
		for c in root.children:
			if(c.visited == False):
				self.DFS(c)

	def BFS(self,root):
		q = Queue()
		root.visited = True
		q.enqueue(root)

		while(not q.isEmpty()):
			r = q.dequeue()
			print(r.data)
			for c in r.children:
				if(c.visited == False):
					c.visited = True
					q.enqueue(c)


#testing
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
a.children.append(b)
a.children.append(c)
b.children.append(d)
b.children.append(e)
c.children.append(f)
c.children.append(g)
d.children.append(h)

ac = copy.copy(a)
ac.BFS(ac)