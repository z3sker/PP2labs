def count(file):
    with open(file, 'r') as file:
        kol = 0
        for i in file:
            kol += 1
    return kol

file = r'C:\Users\z3ske\Desktop\KBTU\PP2labs\lab6\file.txt'
kol = count(file)
print(kol)
