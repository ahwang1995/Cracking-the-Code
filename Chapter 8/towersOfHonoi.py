from Stack import Stack
#solve the towers of honoi problem given these constraints
#there are 3 towers and N disks which start in the first tower
#each tower is represented by a stack and larger discs cannot be set
#on top of larger discs, only one disc can be moved at a time, and only the top can be moved
class towersOfHanoi:
	#initialize the three towers (goal is to move all elements to tower 3)
	def __init__(self,tower1):
		self.tower1 = tower1
		self.tower2 = Stack()
		self.tower3 = Stack()

	def moveDiscs(self,):