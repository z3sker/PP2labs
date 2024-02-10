'''Python Lambda'''

#Syntax

x = lambda a : a + 10
print(x(5))

''''''

x = lambda a, b : a * b
print(x(5, 6))

#Why Use Lambda Functions?
'''The power of lambda is better shown when you use them as an anonymous function inside another function.'''

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

#

