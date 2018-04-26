#given sorted arrays 1 and 2 where array 1 has enough spacce at the end 
#to fit array 2, merge the two arrays
class sortedMerge:
	def sortedM(self,arr1,arr2):
		ind = len(arr1)-1
		arr2Ind = len(arr2)-1
		arr1Ind = ind - arr2Ind
		while(arr2Ind >= 0):
			if arr1Ind >= 0 and a[arr1Ind] > b[arr2Ind]:
				a[ind] = a[arr1Ind]
				arr1Ind = arr1Ind - 1
			else:
				a[ind] = b[arr2Ind]
				arr2Ind = arr2Ind - 1
			ind = ind - 1
