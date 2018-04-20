#find a path from the top left to the bottom right
#of an mxn grid, where some parts of the grid are unable to be
#traversed and the only movements allowed are down and right
class robotInGrid:
	#returns a valid path, or false if there is none
	def findPath(self,grid):
		path = []
		invalidPoints = []

		if self.travelPath(grid,path,invalidPoints,len(grid)-1,len(grid[0])-1):
			return path
		return False

	#recursive function to travel the path, saving invalid points
	def travelPath(self,grid,path,invalidPoints,row,col):
		#if the point is outside of the grid or the coordinate is invalide return false
		if row < 0 or col < 0 or not grid[row][col]:
			return False

		coord = (row,col)
		#return false if the point was already visited
		if coord in invalidPoints:
			return False

		#returns true if the current path is a valid one that reaches the origin
		if (row == 0 and col == 0) or self.travelPath(grid,path,invalidPoints,row-1,col) or \
		 self.travelPath(grid,path,invalidPoints,row,col-1):
		 	path.append(coord)
		 	return True

		#if the current point is not valid move it to the list of invalid points and return false
		invalidPoints.append(coord)
		return False
#test
rig = robotInGrid()
grid = [[0 for i in xrange(3)] for j in xrange(3)]

grid[0][0] = True
grid[0][1] = True
grid[1][1] = True
grid[2][1] = True
grid[2][2] = True

print grid
print(rig.findPath(grid))