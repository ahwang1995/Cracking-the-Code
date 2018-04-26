class rotatedArraySearch:
	#similar to binary search
	def rotatedAS(self,arr,x,low,high):
		mid = (low + high)/2
		if x == arr[mid]: return mid
		if low > high: return False
		#check which side is ordered properly
		if arr[low] < arr[mid]:
			#if the left side is ordered properly, check if it is in the left side, if not search right
			if x >= a[low] and x < a[mid]: return self.rotatedAS(arr,x,low,mid-1)
			else: return self,rotatedAS(arr,x,mid+1,high)
		elif arr[mid] < arr[low]:
			#same for right side
			if x > arr[mid] and a <= arr[high]: return self.rotatedAS(arr,x,mid+1,high)
			else: return self.rotatesAS(arr,x,low,mid-1)
		#if there are duplicate values so the order is not known, check both sides
		elif a[low] == a[mid]:
			if a[mid] != a[right]: return self.rotatedAS(a,mid+1,high,x)
			else:
				result = self.rotatedAS(a,low,mid-1,x)
				if(result == False): return self.rotatedAS(a,mid+1,high,x)
				else: return result
		return False

