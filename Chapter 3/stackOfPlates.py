from Stack import Stack
class stackOfPlates:
	cap = 4
	def _init_(self):
		self.plates = []

	def isEmpty(self):
		return self.plates == []

	def push(self, item):
		p = Stack()
		if (self.plates == []) or (self.plates[0].size() == cap):
			p.push(item)
        	self.plates.append(p)
        else:
        	self.plates[0].push(item)

    def pop(self):
    	for x in self.plates:
    	if not x.isEmpty():
    		return self.plates[0].pop()
    	
    def peek(self):
    	return self.plates[0].peek()

    def size(self):
    	return len(self.plates)

s = stackOfPlates()
s.push(3)
s.push(5)
s.push(1)
s.push(5)
s.push(2)
print(s)
