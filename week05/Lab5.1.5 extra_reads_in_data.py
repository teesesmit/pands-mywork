#Write a program that will read in the data for the data structure from Lab5.1.4
#i.e. reads in a student’s name, then keeps reading in their modules and grades
#(until the user enters a blank module name).
#You can break this up into two parts:
#a. read in the module names until the user enters blank,
#b. Then read in the grade as well
#Author Theresa Smyth

# Start an empty dictionary to store student information
student = {}

# Read in the student's name
student["name"] = input("Enter student's name: ")

# start an empty list to store modules and grades
modules = []

# Read in module names and grades until the user enters a blank module name
while True:
    module_name = input("Enter module name (or leave blank to stop): ")
    if module_name == "":
        break
    grade = int(input(f"Enter grade for {module_name}: "))
    modules.append({"courseName": module_name, "grade": grade})

# Add the modules list to the student dictionary
student["modules"] = modules

# Print the student's information
print("\nStudent: {}".format(student["name"]))
for module in student["modules"]:
    print("\t{}: {}".format(module["courseName"], module["grade"]))