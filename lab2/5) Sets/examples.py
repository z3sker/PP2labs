#1 Python Sets

myset = {"apple", "banana", "cherry"}

#2 Set

thisset = {"apple", "banana", "cherry"}
print(thisset)

#3 Duplicates Not Allowed

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#4 Get the Length of a Set

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#5 Set Items - Data Types

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#6 type()

myset = {"apple", "banana", "cherry"}
print(type(myset))

#7 The set() Constructor

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#8 Access Items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

#9 Add Items

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#10 Add Sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#11 Add Any Iterable

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#12 Remove Item

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#13 Loop Items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

#14 Join Two Sets

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#15 Keep ONLY the Duplicates

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#16 Keep All, But NOT the Duplicates

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)