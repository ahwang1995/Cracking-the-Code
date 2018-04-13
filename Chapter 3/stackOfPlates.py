from Stack import Stack
class stackOfPlates:
	#constructor
	def __init__(self,cap):
		self.plates = []
		self.cap = 4

	#checks if there are no plates
	def isEmpty(self):
		return self.plates == []

	#pushes onto plate or creates new plate
	def push(self, item):
		p = Stack()
		if ((self.isEmpty()) or (self.plates[len(self.plates)-1].size() == self.cap)):
			p.push(item)
			self.plates.append(p)
		else:
			self.plates[len(self.plates)-1].push(item)

	#pops from a plate
	def pop(self):
		if self.isEmpty(): return False
		temp = self.plates[len(self.plates)-1].pop()
		if(self.plates[len(self.plates)-1].isEmpty()): self.plates.pop()
		return temp
	
	#returns top element of the stack
	def peek(self):
		return self.plates[len(self.plates)-1].peek()

	#returns the size of the stack
	def size(self):
		return len(self.plates)

	def popAt(self,ind):
		if self.isEmpty() or self.plates[ind] == None: return False
		temp = self.plates[ind].pop()
		if(self.plates[ind]).isEmpty(): self.plates.remove(self.plates[ind])
		return temp

#Testing
s = stackOfPlates(4)
s.push(3)
s.push(2)
s.push(1)
s.push(4)
s.push(5)
s.push(7)
print(s.popAt(0))



