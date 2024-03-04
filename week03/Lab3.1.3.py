#Lab3.1 Variable and State
#Write a program (div.py) that reads in two numbers and divides the first one by the second 
# and give the integer result and the remainder.
#Author: Theresa Smyth

x = int(input ('Enter first number: '))
y = int(input ('Enter the number you want to divide by: '))
answer = int(x//y) #int division
remainder = x%y #% give the remainder

print("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))