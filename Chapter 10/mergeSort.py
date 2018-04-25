#sort an array by splitting it in halves and merging back together
#from ctci book
class mergeSort:
	def __init(self,arr):
		helperArr = []*len(arr)

	def mergeSort(self,arr,helperArr,start,end):
		if start < end:
			mid = (start + end)/2
			#sort left
			self.mergeSort(arr,helperArr,start,mid)
			#sort right
			self.mergeSort(arr,helperArr,start+1,end)
			#merge
			self.merge(arr,helperArr,start,mid,end)

	def merge(self,arr,helperArr,start,mid,end):
		#put both halves into the helper array
		for i in range(start,end):
			helperArr[i] = array[i]

		helperLeft = start
		helperRight = mid + 1
		curr = start

		#go thorugh the helper array comparing elements from the left and right halves
		#and put the smaller element into the original
		while(helperLeft <= mid and helperRight <= end):
			if helper[helperLeft] <= helper[helperRight]:
				arr[curr] = helper[helperLeft]
				helperLeft = helperLeft + 1
			else:
				arr[current] = helper[helperRight]
				helperRight = helperRight + 1

			curr = curr + 1

		rem = mid - helperLeft
		for i in range(0,rem):
			arr[curr+i] = helper[helperLeft + i]
