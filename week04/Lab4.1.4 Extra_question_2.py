# This program reads in a students percentage 
# Prints out the corresponding grade
# Additional: How would you use a while loop to modify 1 so that it keeps prompting the
#user for a number until the user enters -1.

# Author: Theresa Smyth

#define percentage
percentage = -1

#user enters -1 to stop the loop
while percentage != -1:
    #enter students percentage mark
    percentage = float (input("Enter the percentage (-1 to exit): "))

    #check if -1 is entered to exit the loop
    if percentage == -1:
        break 
    #Round to 1 decimal place
    percentage = round(percentage, 1)
    
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