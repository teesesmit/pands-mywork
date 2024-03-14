# This program reads in a students percentage 
# Prints out the corresponding grade
# Author: Theresa Smyth

percentage = float(input("Enter the percentage: "))
#print (percentage) # this is for dubugging
#Round to nearest whole number
percentage = round(percentage)

# Check if the rounded percentage is between 0-100, if not ask for range
if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100")
elif percentage < 40: # we know it is greater than 0
    print ("Fail")
elif percentage < 50: # between 40 and 49
    print ("Pass")
elif percentage < 60: # between 50 and 59
    print ("Merit1")
elif percentage < 70: # between 60 and 69
    print ("Merit2")
else: # the only option left is betwen 70 and 100
    print ("Distinction")