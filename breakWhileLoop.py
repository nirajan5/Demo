# The control transfer is transfered
# when break statement soon it sees t
i = 0
str1 = 'coventry'

while i < len(str1):
    if str1[i] == 't':
        i += 1
        break
    print('Current Letter :', str1[i])
    i += 1