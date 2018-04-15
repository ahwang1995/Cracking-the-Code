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
				tempVal = heap[curr]
				self.heap[curr] = self.heap[(curr-1)/2]
				self.heap[(curr-1)/2] = tempVal
				curr = (curr-1)/2
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
	def extractMinMax(self,data):
		curr = 0
		#check if empty
		if self.size() == 0:
			return False

		#store return value
		minMax = heap[0]
		elif self.minOrMax == "max":
			self.heap[0] = self.heap.pop(heap[heap.size()-1])
			size = self.heap.size()
			#edge cases
			if size <= 1:
				return True
			if size == 2:
				if self.heap[curr] < self.heap[curr+1]:
					tempVal = self.heap[curr]
					self.heap[curr] = self.heap[curr+1]
					self.heap[curr+1] = tempVal
				return True
			#bubble down
			while (self.heap[curr] < self.heap[curr+1] or self.heap[curr] < self.heap[curr+2]):
				if self.heap[curr+1] < self.heap[curr+2]:
					tempVal = self.heap[curr]
					self.heap[curr] = self.heap[curr+2]
					self.heap[curr+2] = self.heap[curr]
					curr = curr + 2
					size = size - 2

h = minMaxHeap("min")
h.insert(4)
h.insert(7)
h.insert(3)
h.insert(1)
h.insert(5)
h.insert(2)
print h.heap
