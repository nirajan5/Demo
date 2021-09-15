#  open the file.txt in read mode. causes error if no such file exists.
fileptr = open("file2.txt","r")

content = fileptr.read()
print(content)

#  closes the opened file
fileptr.close()