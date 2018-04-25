#pick a random element to partition in the array and repeatedly
#partition by swapping around the element
class quickSort:
	def quickS(self,arr,left,right):
		ind = self.partition(arr,left,right)
		if left < ind - 1:
			self.quickS(arr,left,ind-1)
		if ind < right:
			quickS(arr,ind,right)

	def partition(self,left,right):
		pivot = arr[(left+right)/2]
		while left <= right:
			while arr[left] < pivot: left = left + 1
			while arr[right] > pivot: right = right - 1

			if(left <= right):
				temp = arr[right]
				arr[right] = arr[left]
				arr[left] = temp
		return left
