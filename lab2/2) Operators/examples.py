#Example 1
print(10 + 5)


#Example: Arithmetic Operators
x = 5
y = 10
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)


#Example: Assignment Operators
x = 5
print(x)
x = x + 3	
print(x)
x = x - 3	
print(x)
x = x * 3	
print(x)
x = x / 3	
print(x)
x = x % 3	
print(x)
x = x // 3	
print(x)
x = x ** 3	
print(x)
x = x & 3	
print(x)
x = x | 3	
print(x)
x = x ^ 3	
print(x)
x = x >> 3	
print(x)
x = x << 3
print(x)


#Example: Comparison Operators
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)



#Example: Logical Operators
x = 5
print(x < 5 and  x < 10)	
print(x < 5 or x < 4)	
print(not(x < 5 and x < 10))



#Example: Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

print(x is y)

print(x is not y)



#Example: Membership Operators
x = ["apple", "banana"]
y = ["mango", "apple"]
print("banana" in x)
print(x in y)
print(x not in y)


#Example: Bitwise Operators
x = 4
y = 8
print(x & y)	
print(x | y)	
print(x ^ y)	
print(~x)	
print(x << 2)	
print(x >> 2)