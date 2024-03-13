# Take in a float and outputs an int rounded down
# need the math module math.floor()

# floors a number.
# Author: Theresa Smyth

import math

numberTofloor = float(input("enter a float number:"))
flooredNumber = math.floor(numberTofloor)
print('{} rounded is {}'.format(numberTofloor, flooredNumber))