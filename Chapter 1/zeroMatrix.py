import numpy as np
#If a value in the matrix is zero, set it's row and column values to zero
def zeroMatrix(matr):
	rows,cols = matr.shape
	zrows = np.ones(rows)
	zcols = np.ones(cols)
	#iterate through to find where the zeroes are
	for i in range(0,rows):
		for j in range(0,cols):
			if matr[i,j] == 0:
				zrows[i] = 0
				zcols[j] = 0
	#set the rows and columns of found zeroes to zero
	for i in range(0,rows):
		if zrows[i] == 0: matr[i] = 0
	for i in range(0,cols):
		if zcols[i] == 0: matr[:,i] = 0
	return matr
size = 5
x = np.arange(0,size*size).reshape(size,size)
x[0,0] = 1
x[3,3] = 0
print zeroMatrix(x)
