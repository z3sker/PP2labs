# Python Scope

# Local Scope
# Example: Local variable inside a function
def myfunc():
    x = 300
    print(x)

myfunc()

# Function Inside Function
# Example: Accessing a local variable from a nested function
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

# Global Scope of any function are global and accessible from any scope.
# Example: Global variable
x = 300

def myfunc():
    print(x)

myfunc()

print(x)

# Naming Variables
# Using the same variable name inside and outside a function creates two separate variables.

# Example: Local and global variables with the same name
x = 300

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)

# Global Keyword
# To access or modify a global variable from within a function's local scope, use the global keyword.

# Example: Using the global keyword
def myfunc():
    global x
    x = 300

myfunc()

print(x)

# Example: Changing the value of a global variable inside a function
x = 300

def myfunc():
    global x
    x = 200

myfunc()

print(x)
