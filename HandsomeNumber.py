# Handsome number

number = int(input('Enter number: '))

last_digit = number % 10

left_part = number // 10

left_part_sum = 0
while left_part:
    left_part_sum += left_part % 10
    left_part = left_part // 10

if left_part_sum == last_digit:
    print('%d is Handsome Number.' % number)
else:
    print('%d is Not Handsome Number.' % number)

