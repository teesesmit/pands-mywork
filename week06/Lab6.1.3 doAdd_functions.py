# Functions 
# Keeps displaying the menu until "Q" is picked
# If user chooses "A" then call function doAdd[]
# If user chooses "V" then call function doView[]
# Author Theresa Smyth

# defines display menu function. allows for the output to request information
def displayMenu():
    #prints options for the user to input, (\t = tab aligned)
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    #strip() removes leading and trailing whitespace characters from a string
    choice = input("Type one letter (a/v/q):").strip()
    return choice

#test the function
#choice = displayMenu()
#print("you choose {}".format(choice))
def doAdd():
    print("in adding")
def doView():
    print("in viewing")

#main program
choice = displayMenu()
while(choice != 'q'):
    # could do this with lamda functions below is basic
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu()
    print(f"you choose {choice}")