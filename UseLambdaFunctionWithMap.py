#program to filter out the list which contains odd numbers
lst = (10,20,30,40,50,60)
square_list = list(map(lambda x:x**2,lst))
# the tuple contains all the items of the list for which the lambda function evaluates to true
print(square_list)

