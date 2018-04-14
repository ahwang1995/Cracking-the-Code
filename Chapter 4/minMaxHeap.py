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
			#print self.heap[curr]
			#print self.heap[(curr-1)/2]
			while (self.heap[curr] < self.heap[(curr-1)/2]):
				print("enteredloop")
				tempVal = self.heap[curr]
				print tempVal
				self.heap[curr] = self.heap[(curr-1)/2]
				print self.heap[curr]
				self.heap[(curr-1)/2] = tempVal
				print self.heap[(curr-1)/2]
				curr = (curr-1)/2
				#if at root node then break
				if curr < 1: break
			return True

		return False

	def extractMinMax(self,data):
		pass
h = minMaxHeap("min")
h.insert(4)
h.insert(7)
h.insert(3)
h.insert(1)
h.insert(5)
h.insert(2)
print h.heap
