def printme(name, age=22):
    print("My name is", name, "and age is", age)


printme(name="Krishna")  # the variable age is not passed into the function however the default value of age is considered
printme(age=10, name="Hari")  # the value of age is overwritten here, 10 will be printed as age
