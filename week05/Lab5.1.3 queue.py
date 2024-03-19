#Create a program that puts 10 random numbers into a queue(list)
#the program should then output all the values in the queue
#then take the numbers from the queue one at a time, 
#print it and the current numbers still in the queue.

#Author Theresa Smyth

import random
#initializes an empty list to store numbers
queue = []
#defines variable and sets its value to 10, allows 10 numbers to be generated and add to queue
numberOfNumbers=10
#defines variable and sets to 100, upper limit for the range
rangeTo=100
#starts a loop, generating random numbers and adds to the queue
for n in range(0,numberOfNumbers):
    #inside loop, this generates a random integer between 0 and 'rangeto' and appends to list
    queue.append(random.randint(0,rangeTo))
#after generating the random numbers, this prints the contents of the "queue" list
print (f"queue is {queue}")
#starts loop that continues until list becomes empty (0)
while len(queue) != 0:
#Inside the loop, removes the first element from the queue list using pop(0) 
#and assigns it to the variable currentNumber. 
#This simulates a First-In-First-Out queue behavior.
    currentNumber = queue.pop(0)
print ("current Number is {currentNumber} and the queue is {queue} ")
print ("the queue is now empty")