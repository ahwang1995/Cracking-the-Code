from Node import Node
import itertools
#return every possible array in which the tree could have been ordered
class bstSequences:
	#recursive function to add arrays
	def makeArrayLeft(self,root,array):

		tempArray = array[len(array)-1]
		if root.left != None:
			tempArray.append(root.left.data)
			array.append(tempArray)
			self.makeArrayLeft(root.left,tempArray)
		if root.right != None:
			tempArray.append(root.right.data)
			array.append(tempArray)
			self.makeArrayLeft(root.right,tempArray)

	def makeArrayRight(self,root,array):

		tempArray = array[len(array)-1]

		if root.right != None:
			tempArray.append(root.right.data)
			array.append(tempArray)
			self.makeArrayRight(root.right,tempArray)

		if root.left != None:
			tempArray.append(root.left.data)
			array.append(tempArray)
			self.makeArrayRight(root.left,tempArray)


	def getSequences(self,root):
		leftArr = [[root.data]]
		rightArr = [[root.data]]

		self.makeArrayLeft(root,leftArr)
		self.makeArrayRight(root,rightArr)

		arr = leftArr + rightArr
		#remove duplicates
		arr.sort()
		arr = list(arr for arr,_ in itertools.groupby(arr))

		return arr

n = Node(2)
n.left = Node(1)
n.right = Node(3)
bstS = bstSequences()
print(bstS.getSequences(n))