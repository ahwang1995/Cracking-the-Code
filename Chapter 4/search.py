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

	def BFS
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

a.DFS(a)