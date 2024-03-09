# Python Modules

# Creating a Module
# Example: Creating a module named mymodule.py
def greeting(name):
    print("Hello, " + name)

# Using a Module
# Modules can be used by importing them using the import statement.

# Example: Importing and using the greeting function from mymodule
import mymodule

mymodule.greeting("Jonathan")

# Variables in Module
# Modules can contain variables of various types.

# Example: Using variables from a module
import mymodule

a = mymodule.person1["age"]
print(a)

# Naming a Module
# Module filenames must have the .py extension.

# Re-naming a Module
# Modules can be imported with aliases using the as keyword.

# Example: Importing and aliasing a module
import mymodule as mx

a = mx.person1["age"]
print(a)

# Built-in Modules
# Python includes several built-in modules that can be imported as needed.

# Example: Importing and using the platform module
import platform

x = platform.system()
print(x)

# Using the dir() Function
# The dir() function lists all function or variable names in a module.

# Example: Using the dir() function on the platform module
import platform

x = dir(platform)
print(x)

# Import From Module
# Specific parts of a module can be imported using the from keyword.

# Example: Importing only the person1 dictionary from mymodule
from mymodule import person1

print(person1["age"])
