from Node import Node
#a child's parent is at (i-1)/2
#the left and right children are at 2i+1 and 2i+2 respectively
class minMaxHeap:
	#constructor with parameter specifying whether it is a min or max heap
	def __init__(self,minOrMax,heap=None):
		self.heap = []
		self.minOrMax = minOrMax

	#check if heap is empty
	def isEmpty(self):
		return self.heap == []

	#check size of the heap
	def size(self):
		return len(self.heap)

	#insert an element into the heap
	def insert(self,data):
		curr = self.size()
		#if the heap is initially empty, append element
		if self.size() == 0:
			self.heap.append(data)

		#check if it is a min or max heap insert and bubble up
		elif self.minOrMax == "max":
			self.heap.append(data)
			while (self.heap[curr] > self.heap[(curr-1)/2]):
				tempVal = self.heap[curr]
				self.heap[curr] = self.heap[(curr-1)/2]
				self.heap[(curr-1)/2] = tempVal
				curr = (curr-1)/2
				if curr < 1: break
			return True

		elif self.minOrMax == "min":
			self.heap.append(data)
			while (self.heap[curr] < self.heap[(curr-1)/2]):
				tempVal = self.heap[curr]
				self.heap[curr] = self.heap[(curr-1)/2]
				self.heap[(curr-1)/2] = tempVal
				curr = (curr-1)/2
				#if at root node then break
				if curr < 1: break
			return True

		return False

	#remove top element and resort heap
	def extractMinMax(self):
		curr = 0
		#check if empty
		if self.size() == 0:
			return False

		#store return value
		minMax = self.heap[0]
		self.heap[0] = self.heap.pop(self.heap[self.size()-1])
		#bubble down
		self.trickleDown(0)
		return minMax

	#trickle down helper method
	def trickleDown(self,index,):
		c1Index = index*2 + 1
		c2Index = index*2 + 2

		if c1Index >= self.size():
			return

		parent = self.heap[index]
		child1 = self.heap[c1Index]
		child2 = child1

		if c2Index < self.size():
			child2 = self.heap[c2Index]

		if self.minOrMax == "max":
			if child1 >= child2 and child1 > parent:
				self.heap[c1Index] = parent
				self.heap[index] = child1
				self.trickleDown(c1Index)
			if child2 > child1 and child2 > parent:
				self.heap[c2Index] = parent
				self.heap[index] = child2
				self.trickleDown(c2Index)
		
		if self.minOrMax == "min":
			if child1 <= child2 and child1 < parent:
				self.heap[c1Index] = parent
				self.heap[index] = child1
				self.trickleDown(c1Index)
			if child2 < child1 and child2 < parent:
				self.heap[c2Index] = parent
				self.heap[index] = child2
				self.trickleDown(c2Index)
		return

h = minMaxHeap("max")
h.insert(4)
h.insert(7)
h.insert(3)
h.insert(1)
h.insert(5)
h.insert(2)
print(h.extractMinMax())
print h.heap
