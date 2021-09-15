# open the file.txt in append mode. Create a new file if no such file exists.
fileptr = open("file2.txt", "w")

# appending the content to the file
fileptr.write('''''Python is one of the popular programming language. It is gaining popular worldwide.
                 It has its applications in many fields.''')

# closing the opened the file
fileptr.close()
