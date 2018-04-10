import numpy as np
#rotate an image/matrix 90 degrees
def rotImg(img):
	layer,asdf = img.shape
	#check layer by layer, outside to inside up to half
	for i in range(0,layer/2):
		#variables for first and last layers
		first = i
		last = layer - 1 - i
		#for each pixel in the layer rotate it
		for j in range(first,last):
			offset = j - first
			top = img[first,j]
			img[first,j] = img[last-offset,first]
			img[last-offset,first] = img[last,last-offset]
			img[last,last- offset] = img[j,last]
			img[j,last] = top
	return img
size = 3
x = np.arange(0,size*size).reshape(size,size)
print rotImg(x)
