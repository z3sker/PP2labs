#1 List

mylist = ["apple", "banana", "cherry"]

#2 List

thislist = ["apple", "banana", "cherry"]
print(thislist)
 
#3 Allow Duplicates

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#4 List Length

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#5 List Items - Data Types

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

''''''

list1 = ["abc", 34, True, 40, "male"]

#6 type()

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#7 The list() Constructor

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#8 Access Items

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#9 Negative Indexing

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#10 Range of Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

''''''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

''''''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#11 Range of Negative Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#12 Check if Item Exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#13 Change Item Value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#14 Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

''''''

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)