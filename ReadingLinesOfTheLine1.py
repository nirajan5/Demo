# open the file.txt in read mode. causes error if no such file exists.
fileptr = open("file2.txt", "r")
# stores all the data of the file into the variable content
content = fileptr.readline()
content1 = fileptr.readline()
# prints the content of the file
print(content)
print(content1)
# closes the opened file
fileptr.close()
