#We can now write the function doAdd(students).
#a. Read in the student’s name 
#b. Read in the module names and grades
#c. Test this function, it creates a student dict, print that out.
#d. We should add the student dict to list (pass this list in)
#Author Theresa Smyth

#defines function
def readModules():
    #empty list
    return []
#defines a function - expected to be a list
def doAdd(students):
    #inside the function empyty dictionary called:
    currentStudent = {}
    #promts user to enter a name and enters a name to the name key of the currentStudents dict
    currentStudent["name"]=input("enter name :")
    #calls the readmodules function to get a list of modules for the student and assigns
    #the returned list to the modules key of the currentstudent dict
    currentStudent["modules"]= readModules()
    #appends the currentstudent dict to the students list passed as an argument to the function
    students.append(currentStudent)
#test it, empty list named stdents that will hold infor about the students and thier modules
students = []
#adds student (name and modules) to the student list
doAdd(students)
#adds 2nd student (name and modules) to the student list
doAdd(students)
print(students)