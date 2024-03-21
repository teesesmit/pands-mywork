#Find error
#Error with quotes
#Author Theresa Smyth

def displayModules(modules):
    print ("\tName   \tGrade")
    for module in modules:
        #Double quotes and single quotes required
        print(f"\t{module['name']}  \t{module['grade']}") 


def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]);
