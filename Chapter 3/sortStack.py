from Stack import Stack
#sort a stack using a tempstack so that the smallest elements are at the top
class sortStack:
	def sortS(self,s):
		finalSize = s.size()
		tempS = Stack()
		if s.isEmpty(): return False
		#iterate through the initial stack
		while not ((s.isEmpty())):
			#if the temp stack is full then sorting is complete
			if tempS.size() < finalSize:
				#store the element popped from the initial stack
				tempNode = s.pop()
				#if the element is smaller then the top of tempstack, then push to temp
				if (tempS.isEmpty()) or (tempNode <= tempS.peek()):
					tempS.push(tempNode)
				#else push the node on top of temp onto the original stack and, then push tempNode to tempStack
				else:
					s.push(tempS.pop())
					tempS.push(tempNode)
		return tempS
#testing
unsorted = Stack()
unsorted.push(5)
unsorted.push(7)
unsorted.push(3)
sorter = sortStack()
sortedS = sorter.sortS(unsorted)

while not sortedS.isEmpty():
	a = sortedS.pop()
	print(a)
