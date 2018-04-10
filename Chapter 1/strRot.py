#check if a string is the rotation of another
def strRot(str1,str2):
	len1 = len(str1)
	if(len1 == len(str2) and len1 > 0):
		return str2 in (str1 + str1)
	return False 
print strRot("asdafg","gafsdf")
