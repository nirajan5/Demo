# Python program to find sum of elements in list
total = 0

# creating a list
list1 = [12, 5, 25, 18, 44]

# Iterate each element in list
# and add all of them in variable total
for i in range(0, len(list1)):
    total = total + list1[i]

# printing total value
print("Sum of all elements in given list: ", total)
