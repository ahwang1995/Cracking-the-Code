from search import Node
from Queue import Queue
class routeBetweenNodes:
	#just a BFS which checks to see if route is found
	def routeBN(self,root,nodeB):
		q = Queue()
		root.visited = True
		q.enqueue(root)

		while(not q.isEmpty()):
			r = q.dequeue()
			for c in r.children:
				if(c.visited == False):
					c.visited = True
					if c.data == nodeB.data: return True
					q.enqueue(c)
		return False

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

rBN = routeBetweenNodes()
print(rBN.routeBN(g,a))