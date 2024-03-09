import os

def proverka(path):
    if os.path.exists(path):
        papka, file = os.path.split(path)
        return papka, file
    else:
        return None, None

path = r"C:\Users\z3ske\Desktop\KBTU\PP2labs\lab6"

papka, file = proverka(path)

if papka and file:
    print("Path exists.")
    print("Directory:", papka)
    print("Filename:", file)
else:
    print("Path does not exist.")