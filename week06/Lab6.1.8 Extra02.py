#Extra 
#Variables can be of type function and we call those variables
#lists, tuples and dicts can have variables of type function in them,
#so we could have dict that stores the letter of the menu and the function associated with
#that letter. We could access that function by that letter

#defines fun1 and fun2 and prints out this is fun1/2
def fun1():
    print("this is fun1")
def fun2():
    print("this is fun2")

#assigns the function fun1 to the variable 'whichfun'.
#this means 'whichfun' now references the fun1() function
whichFun = fun1
#Calls the function that whichFun references, which is fun1(). So, when whichFun() is called, 
#it executes the code inside the fun1() function and prints "this is fun1".
whichFun()

#Reassigns the variable whichFun to reference the fun2() function. 
#Now, whichFun refers to the fun2() function.
whichFun= fun2
#Calls the function that whichFun now references, which is fun2(). So, when whichFun() is 
#called again, it executes the code inside the fun2() function and prints "this is fun2".
whichFun()