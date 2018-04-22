#print all valid parentheses combinations given n pairs
class parens:
	#builds combinations parenthesis
	def parenCombs(self,n):
		string = [None]*(n*2)
		combs = []
		self.addParen(combs,n,n,string,0)
		return combs

	#uses recursion to build the combinations, add left parenth then add right
	def addParen(self,combs,left,right,string,ind):
		#cannot add right parenthesis while there are no left ones or there are less right ones available
		#left and right are the remaining left and right parenthesis available, cannot have less right then left
		if left < 0 or right < left: return

		#base case
		if(left == 0 and right == 0):
			combs.append(str(string))

		#recurse	
		else:
			string[ind] = '('
			self.addParen(combs,left-1,right,string,ind+1)

			string[ind] = ')'
			self.addParen(combs,left,right-1,string,ind+1)

p = parens()
print(p.parenCombs(3))