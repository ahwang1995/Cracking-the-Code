class sparseSearch:
	#similar to binary search
	def sparseS(self,arr,string,first,last):
		if first > last: return False
		mid = (first + last)/2

		#search surrounding strings next to mid
		if arr[mid] == "":
			left = mid-1
			right = mid+1
			while True:
				if(left < first and right > last): return False
				elif(right <= last and arr[right] != ""):
					mid = right
					break
				elif(left >= first and arr[left] != ""):
					mid = left
					break
				right = right + 1
				left = left - 1

		if string == arr[mid]: return mid
		elif arr[mid] < string: return self.sparseS(arr,string,mid + 1,last)
		else: return self.sparseS(arr,string,first,mid-1)

#test
arr = ["asdf","","","","fdsa","","","","jkl","","","qwer"]

ss = sparseSearch()
print ss.sparseS(arr,"jkl",0,len(arr)-1)