from Stack import Stack
#solve the towers of honoi problem given these constraints
#there are 3 towers and N disks which start in the first tower
#each tower is represented by a stack and larger discs cannot be set
#on top of larger discs, only one disc can be moved at a time, and only the top can be moved
class towersOfHanoi:
	#recursive function to move discs from a to b using c
	def moveDiscs(self,n,a,b,c):
		#base case
		if n == 1: return

		#move rods 1 by 1 using recursion
		self.moveDiscs(n-1,a,b,c)
		if not a.isEmpty():
			b.push(a.pop())
		self.moveDiscs(n-1,c,b,a)

a = Stack()
b = Stack()
c = Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
n = a.size()
toh = towersOfHanoi()
toh.moveDiscs(n,a,b,c)

while not b.isEmpty():
	print(b.pop())