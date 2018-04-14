from Node import Node
#a child's parent is at (i-1)/2
#the left and right children are at 2i+1 and 2i+2 respectively
class minMaxHeap:
	#constructor with parameter specifying whether it is a min or max heap
	def __init__(self,MinOrMax,heap=None):
		self.heap = []
		self.MinOrMax = MinOrMax

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

		#check if it is a min or max heap then bubble up
		if minOrMax == "max":
			self.heap.append(data)
			while (heap[curr] > heap[(curr-1)/2]):
				tempVal = heap[curr]
				heap[curr] = heap[(curr-1)/2]
				heap[(curr-1)/2] = tempVal
				curr = (curr-1)/2
			return True

		elif minOrMax == "min":
			self.heap.append(data)
			while (heap[curr] < heap[(curr-1)/2]):
				tempVal = heap[curr]
				heap[curr] = heap[(curr-1)/2]
				heap[(curr-1)/2] = tempVal
				curr = (curr-1)/2
			return True

		return False

	def extractMinMax(self,data):
		pass