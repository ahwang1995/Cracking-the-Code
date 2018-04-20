#given a sorted array find the magic index, which is when the
#element is equal to it's index
#do this for the case where the array has distinct element and if it doesn't
class magicIndex:
	#returns the magic index if there is one
	def magInd(self,arr):
		return self.searchIndDist(arr,0,len(arr)-1)
	#similar to binary search, find the magic index with a distinct array
	def searchIndDist(self,arr,start,end):
		if(end < start):
			return False

		mid = (start+end)/2

		if(arr[mid] == mid):
			return mid

		elif(arr[mid] > mid):
			return self.searchIndDist(arr,start,mid-1)

		else:
			return self.searchIndDist(arr,mid + 1,end)

#test
mi = magicIndex()
arr = [-5,-3,0,1,3,5,6,9,11,15]
print mi.magInd(arr)