# take an input of an amount in the form 9.44 (9 dollars and 44 cent)
# Could be negative/positive number 
# takes in a float amount of dollars and returns that amount in cent.
# Author: Theresa Smyth

def dollars_to_cents(amount): 
# converts amount to cents
    cents = int(amount * 100)
    return cents

# input amount in dollars
amount_in_dollars = float(input("Enter the amount in dollars: "))

# Convert dollars to cents
amount_in_cents = dollars_to_cents(amount_in_dollars)

# Print the amount in cents
print("Amount in cents:", amount_in_cents)
