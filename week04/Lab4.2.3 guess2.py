#Promts a user till guess a number
#Program to tell user guess too high/low each time they guess

#Author Theresa Smyth

import random

#gererate number 0-100
numberToGuess = random.randint(0,100)

while True:
    guess = int(input("Please guess the number between 0 to 100:"))
    if guess == numberToGuess:
        print("Well done! Yes the number was ", numberToGuess)
        break
    elif guess < numberToGuess:
        print("Too low")
    else:
        print("Too High")