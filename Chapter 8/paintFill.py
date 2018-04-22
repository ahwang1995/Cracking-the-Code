#fills the pixels in a matrix that is not cut off by other colors
class color:
	black = 1
	white = 2
	red = 3
	blue = 4
	green = 5
class paintFill:
	#similar to dfs
	def fill(self,image,row,col,newColor):
		#the point being filled is already that color
		if image[row][col] == color: return False
		return self.fillSearch(image,row,col,image[r][c],newColor)

	def fillSearch(self,image,row,col,origColor,newColor):
		if row < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
			return False

		if (screen[row][col] == origColor):
			screen[row][col] = newColor
			self.fillSearch(image,row-1,col,origColor,newColor)
			self.fillSearch(image,row+1,col,origColor,newColor)
			self.fillSearch(image,row,col-1,origColor,newColor)
			self.fillSearch(image,row,col+1,origColor,newColor)
		return True