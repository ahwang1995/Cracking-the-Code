#replaces spaces with %20
def URLify(str):
	newstr = str.replace(" ","%20")
	return newstr
print URLify("yu")