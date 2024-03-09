import string

def files():
    for i in string.ascii_uppercase:
        filename = f"{i}.txt"
        with open(filename, 'w') as file:
            pass

files()
print("files was created")
