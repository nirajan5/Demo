
# Finding most occurring character

# Get string from user
string = input("Enter some text: ")

# Set frequency as empty dictionary
frequency_dict = {}

for character in string:
    if character in frequency_dict:
        frequency_dict[character] += 1
    else:
        frequency_dict[character] = 1

most_occurring = max(frequency_dict, key=frequency_dict.get)

# Displaying result
print("\nMost occurring character is: ", most_occurring)
print("It is repeated %d times" %(frequency_dict[most_occurring]))

