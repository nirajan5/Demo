# open the file file2.txt in read mode
fileptr = open("file2.txt", "r")

# initially the filepointer is at 0
print("The filepointer is at byte :", fileptr.tell())

# changing the file pointer location to 10.
fileptr.seek(10)

# tell() returns the location of the fileptr.
print("After reading, the filepointer is at:", fileptr.tell())

