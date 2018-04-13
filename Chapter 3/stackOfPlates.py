from Stack import Stack
class stackOfPlates:
	def __init__(self,cap):
		self.plates = []
		self.cap = 4

	def isEmpty(self):
		return self.plates == []

	def push(self, item):
		p = Stack()
		if ((self.isEmpty()) or (self.plates[len(self.plates)-1].size() == self.cap)):
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

s = stackOfPlates(4)
s.push(3)
s.push(2)
s.push(1)
s.push(4)
s.push(5)
s.push(7)
while not s.isEmpty():
	a = s.pop()
	print(a)


