import random
x = 1
y = 6

roll_again = "y"
while roll_again == "y" or roll_again == "yes":
    print("Rolling the dices...")
    print("The values are....")
    die1 = (random.randint(x, y))
    die2 = (random.randint(x, y))
    print(die1, die2)
    if (die1 + die2) == 7 or (die1 + die2) == 11:
        print("You win!")
    else:
        print("you lost")
    roll_again = input("Roll the dices again?")
