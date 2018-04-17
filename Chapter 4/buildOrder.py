import copy
from search import Node
from collections import defaultdict
from Stack import Stack
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
	def DFS(self,root,vals):
		if (root == None): return
		if(root.visit == "visted"): return
		root.visit = "tempvisit"
		for c in root.children:
			print c.data
			if self.proj[c.data].visit == "tempvisit": return False
			if(self.proj[c.data].visit == "unvisited"):
				self.DFS(self.proj[c.data],vals)
			self.proj[c.data].visit = "visited"
			vals.append
			print("asdf")

		return True

	def buildOrder(self,projects,dependencies):
		self.addVerts(projects)
		self.addEdges(dependencies)
		foundVals = []
		for n in self.proj:
			if not self.DFS(self.proj[n],foundVals):
				print (foundVals)
				return False

projs = ["a","b","c","d","e","f"]
depends = [("a","d"),("f","b"),("b","d"),("f","a"),("d","c")]
bo = directedGraph()
print(bo.buildOrder(projs,depends))

