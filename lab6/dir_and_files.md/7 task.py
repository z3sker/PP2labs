def copy_file(file, new_file):
    with open(file, 'r') as i:
        with open(new_file, 'w') as j:
            j.write(i.read())

file = r'C:\Users\z3ske\Desktop\KBTU\PP2labs\lab6\file.txt'
new_file = r'C:\Users\z3ske\Desktop\KBTU\PP2labs\lab6\new_file.txt'

copy_file(file, new_file)
