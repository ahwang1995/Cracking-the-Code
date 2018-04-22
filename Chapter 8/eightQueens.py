from copy import copy
class eightQueens:
	board = 8
	#place the queens recursively
	def placeQueen(self,row,cols,ret):
		if row == board:
			ret.append(copy.copy(cols))
		else:
			for col in range(0,board):
				if self.checkQueen(cols,row,col):
					cols[row] = col
					self.placeQueen(row+1,cols,ret)

	#check if this is a valid spot to place the queen
	#make sure nothing is in the same row or the same diagnol
	def checkQueen(self,cols,row1,col1):
		for row2 in range(0,row1):
			col2 = cols[row2]

		if col1 == col2: return False

		colDist = abs(col2-col1)
		rowDist = row2-row1
		if colDist == rowDist: return False

		return True