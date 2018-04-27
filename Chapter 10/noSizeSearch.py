#binary search on a sorted array with no access to it's size and only positive integers
class noSizeSearch:
	#return -1 if index is out of bounds
	def getElement(self,arr,x):
		try:
			return arr[x]
		except IndexError:
			return -1
	#find when either the array ends or the segment where element is in is found
	def findLenS(self,arr,x):
		ind = 1
		while self.getElement(arr,ind) != -1 and self.getElement(arr,ind) < x:
			ind = ind*2
		return self.binS(arr,x,ind/2,ind)

	#binary search on a portion of the array
	def binS(self,arr,x,left,right):
		while left <= right:
			mid = (left + right)/2
			midElem = self.getElement(arr,mid)
			if midElem > x or midElem == -1:
				right = mid - 1
			elif midElem < x:
				left = mid + 1
			else: return mid
		return -1
#Test
nss = noSizeSearch()
print nss.findLenS([3,4,5,6],5)

