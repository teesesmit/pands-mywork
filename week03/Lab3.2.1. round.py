# Rounds a number.
# Be careful of round, it rounds to the nearest even number 
# eg 4.5 rounds to 4,
# but 5.5  rounds to 6,
# so do not use it accuracy is essential.
#
#Author: Theresa Smyth

numberToRound = float(input("Enter a float number:")) #float decimal values/fractional numbers
roundedNumber = round(numberToRound) #round - rounds nearest even number!

print ( '{} rounded is {}'.format(numberToRound,roundedNumber))