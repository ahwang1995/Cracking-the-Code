from collections import deque
#directedgraph class to implement buildOrder
class directedGraph:
	#use a hashtable for the graph
	def __init__(self):
		self.proj = {}

	#add a vertice to the graph
	def addVerts(self,vert):
		for v in vert:
			if(v not in self.proj):
				n = Node()
				n.data = v
				self.proj[v] = n

	#add an edge to the graph
	def addEdges(self,depen):
		for d in depen:
			self.proj[d[1]].children.append(self.proj[d[0]])

	#depth first search
	def DFSModified(self,root,projs,depends,temps,perms,vals):
		if root in temps: return False
		if root not in perms:
			temps.append(root)
			for d in depends:
				if d[0] == root:
					self.DFSModified(d[1],projs,depends,temps,perms,vals)
			perms.append(root)
			temps.remove(root)
			vals.append(root)

	def buildOrder(self,projects,dependencies):
		tempMarks = []
		permMarks = []
		vals = deque()

		for p in projects:
			if p not in permMarks:
				self.DFSModified(p,projects,dependencies,tempMarks,permMarks,vals)
		return vals

projs = ["a","b","c","d","e","f"]
depends = [("a","d"),("f","b"),("b","d"),("f","a"),("d","c")]
bo = directedGraph()
print(bo.buildOrder(projs,depends))

