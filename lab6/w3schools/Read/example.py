# Python File Open

# The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("demofile.txt", "r")
print(f.read())


# If the file is located in a different location, you will have to specify the file path, like this:
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())


# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
# Return the 5 first characters of the file:
f = open("demofile.txt", "r")
print(f.read(5))


# Read Lines
# You can return one line by using the readline() method:
f = open("demofile.txt", "r")
print(f.readline())


# By calling readline() two times, you can read the two first lines:
# Read two lines of the file:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())


# By looping through the lines of the file, you can read the whole file, line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)


# Close Files
f = open("demofile.txt", "r")
print(f.readline())
f.close()
