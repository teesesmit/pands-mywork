# User enter a number 
# Program indicates if the number is odd or even
# Using "if" statments
# Author: Theresa Smyth

#enter number
number = int(input("enter an integer:"))

# if the number is divisible by 2 it's even, if it doesn't then it's not
if (number % 2) == 0:
    print (f"{number} is an even number")
else:
    print(f"{number} is an odd number")