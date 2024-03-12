#Lab3.1 Variable and State
#Write a program (randomGenerator.py) that prints out a random number between 1 and 10
#Author: Theresa Smyth


import random
number = random.randint(1,10)

print('here is a random number {}'. format(number))

# User inputs the range

x =int(input('Type a number to start the range: ')) #enter start
y =int(input('Type a number to end the range: ')) #enter end

print(range(x, y))




 