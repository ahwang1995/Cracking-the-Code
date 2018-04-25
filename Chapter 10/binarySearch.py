class binarySearch:
	#iterative solution
	def binaryS(self,arr,x):
		low = 0
		high = len(arr)-1
		mid = None
		while low <= high:
			mid = (low + high)/2
			if arr[mid] < x:
				low = mid + 1
			elif a[mid] > x: high = mid - 1
			else: return mid
		return False

	#recursive solution
	def binarySR(self,x,low,high):
		if low > high: return False
		mid = (low + high)/2
		if arr[mid] < x:
			return self.binarySR(a,x,mid+1,high)
		elif arr[mid] > x:
			return self.binarySR(a,x,low,mid-1)
		else:
			return mid