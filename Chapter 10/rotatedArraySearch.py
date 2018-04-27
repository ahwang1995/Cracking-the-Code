class rotatedArraySearch:
	#similar to binary search
	def rotatedAS(self,arr,x,low,high):
		mid = (low + high)/2
		if x == arr[mid]: return mid
		if low > high: return False
		#check which side is ordered properly
		if arr[low] < arr[mid]:
			#if the left side is ordered properly, check if it is in the left side, if not search right
			if x >= arr[low] and x < arr[mid]: return self.rotatedAS(arr,x,low,mid-1)
			else: return self.rotatedAS(arr,x,mid+1,high)
		elif arr[mid] < arr[low]:
			#same for right side
			if x > arr[mid] and arr <= arr[high]: return self.rotatedAS(arr,x,mid+1,high)
			else: return self.rotatedAS(arr,x,low,mid-1)
		#if there are duplicate values so the order is not known, check both sides
		elif arr[low] == arr[mid]:
			if arr[mid] != arr[high]: return self.rotatedAS(arr,mid+1,high,x)
			else:
				result = self.rotatedAS(arr,low,mid-1,x)
				if(result == False): return self.rotatedAS(arr,mid+1,high,x)
				else: return result
		return False

arr = [5,6,7,2,3,4]
arr2 = [2,2,2,2,3,4,1]
ras = rotatedArraySearch()
print ras.rotatedAS(arr2,3,0,len(arr2)-1)