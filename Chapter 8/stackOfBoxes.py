class box:
	def __init__ (self,height=None,length=None,width=None):
		self.height = height
		self.length = length
		self.width = width

	def striclyGreater(self,box2):
		if self.height > box2.height and self.length > box2.length \
		and self.width > box2.width:
			return True
		return False

#get the tallest stack boxes such that each box on top of another is
#strictly smaller in width length and height
class stackOfBoxes:
	def tallestStack(self,boxArr):
		sortedBoxes = sorted(boxArr,key = lambda box: box.height, reverse = True)
		maxHeight = 0
		stackMap = []*len(boxArr)
		return makeStack(boxArr,None,0,stackMap)

	#recursive function to build stacks, sort by 1 paramenter since it needs to be strictly greater
	def makeStack(self,boxArr,bottom,offset,stackMap):
		#base case
		if offset >= len(boxArr): return 0

		currBot = boxArr(offset)
		heightWithBot = 0
		if bottom == None or currBot.striclyGreater(bottom):
			if stackMap[offset] == 0:
				stacMap[offset] = makeStack(boxArr,currBot,offset + 1,stackMap)
				stackMap[offset] = stackMap[offset] + currBot.height
			heightWithBot = stackMap[offset]

		#with a different bottom
		heightWithoutBot = makeStack(boxArr,bottom,offset + 1, stackMap)
		return max(heightWithBot,heightWithoutBot)

#test
boxArr = []
for i in xrange(0,5):
	x = box(i,i,i)
	boxArr.append(x)


a = sorted(boxArr,key=lambda box: box.height, reverse = True)
