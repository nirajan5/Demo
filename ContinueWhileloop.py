# prints all letters except 'a' and 't'
i = 0
str1 = 'softwarica'

while i < len(str1):
    if str1[i] == 'a' or str1[i] == 't':
        i += 1
        continue
    print('Current Letter :', str1[i])
    i += 1