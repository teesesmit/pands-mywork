#Promts a user ti guess a number
#Program to keep promting until the user guesses correctly.

#Author Theresa Smyth

#defines the variable as 30
numberToGuess = 30
#defining guess, Input a guess, coverts to int
guess = int(input("Please guess the number:"))
#while Loop until the user enters 30
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))
print ("Well done! Yes the number was", numberToGuess)