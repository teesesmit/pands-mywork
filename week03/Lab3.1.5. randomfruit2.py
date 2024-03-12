# Lab3.1 Variable and State
# Write a program (randomfruit2.py) that prints out a random fruit using tuple ( ) not a list [ ]
# Author: Theresa Smyth

# This program prints out a random fruit

import random

fruits = ('Apple', 'Orange', 'Banana', 'Pear')

# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]

print("A Random Fruit:{}".format(fruit))