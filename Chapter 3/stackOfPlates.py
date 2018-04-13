from Stack import Stack
class stackOfPlates:
	cap = 4
	def _init_(self):
		self.plates = []

	def isEmpty(self):
		return self.plates == []

	def push(self, item):
		p = Stack()
		if ((self.isEmpty()) or (self.plates[len(self.plates)-1].size() == cap)):
			p.push(item)
			self.plates.append(p)
		else:
			self.plates[len(self.plates)-1].push(item)

	def pop(self):
		temp = self.plates[len(self.plates)-1].pop()
		if(self.plates[len(self.plates)-1].isEmpty()): self.plates.pop()
		return temp
		
	def peek(self):
		return self.plates[len(self.plates)-1].peek()

	def size(self):
		return len(self.plates)

s = stackOfPlates()
s.push(3)

