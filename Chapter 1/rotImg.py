import numpy as np
def rotImg(img):
	layer,asdf = img.shape
	for i in range(0,layer/2):
		first = i
		last = layer - 1 - i
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
