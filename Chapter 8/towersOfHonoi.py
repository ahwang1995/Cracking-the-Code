from Stack import Stack
#solve the towers of honoi problem given these constraints
#there are 3 towers and N disks which start in the first tower
#each tower is represented by a stack and larger discs cannot be set
#on top of larger discs, only one disc can be moved at a time, and only the top can be moved
class towersOfHanoi:
	#recursive function to move discs
	def moveDiscs(self,n,a,b,c):
		#base case
		if n == 1: 
			c.push(a.pop())
			return

		#move rods 1 by 1 using recursion
		self.moveDiscs(n-1,a,c,b)
		if not a.isEmpty():
			c.push(a.pop())
		self.moveDiscs(n-1,b,a,c)

a = Stack()
b = Stack()
c = Stack()
a.push(4)
a.push(3)
a.push(2)
a.push(1)
n = a.size()
toh = towersOfHanoi()
toh.moveDiscs(n,a,b,c)

while not c.isEmpty():
	print(c.pop())