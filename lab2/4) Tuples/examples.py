'''Python Tuples'''

#1 Tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#2 Allow Duplicates

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#3 Tuple Length

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#4 Create Tuple With One Item

thistuple = ("apple",)
print(type(thistuple))

'''NOT a tuple'''
thistuple = ("apple")
print(type(thistuple))

#5 Tuple Items - Data Types

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#6 type()

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#7 The tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#8 Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#9 Loop Through a Tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#10 Join Two Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#11 Unpacking a Tuple

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#12 Change Tuple Values

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)