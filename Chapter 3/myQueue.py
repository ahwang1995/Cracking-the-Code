from Stack import Stack
#create a queue using 2 stacks
class myQueue:
	def __init__(self,s1=None,s2=None):
		self.s1 = Stack()
		self.s2 = Stack()

	def isEmpty(self):
		return (s1.isEmpty() and s2.isEmpty())

	def enqueue(self,item):
		s1.push(item)

	def dequeue(self):
		if(s2.isEmpty()):
			while not s1.isEmpty():
				s2.push(s1.pop())
		return s2.pop()
	
	def size(self):
		return s1.size() + s2.size()


