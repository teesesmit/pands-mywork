#From last week "student" programe
#Create a program that allows a user to create new students and to view students
# Functions 
# Author Theresa Smyth

# defines display menu function
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
choice = displayMenu()
print(f"you chose {choice}")