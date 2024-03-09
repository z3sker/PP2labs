import os
#==================================================
def papki_files(path):
    directories = []
    files = []

    all = os.listdir(path)

    for i in all:
        item_path = os.path.join(path, i)
        if os.path.isdir(item_path):
            directories.append(i)
        elif os.path.isfile(item_path):
            files.append(i)

    return directories, files
#==================================================
def vsechtoest(path):
    all = []

    for root, papki, files in os.walk(path):
        for papka in papki:
            all.append(os.path.join(root, papka))
            
        for file in files:
            all.append(os.path.join(root, file))

    return all
#==================================================
path = r"C:\Users\z3ske\Desktop\KBTU\PP2labs\lab6"

papki, files = papki_files(path)

print("Papki:\n")
print(papki, end = "\n\n")

print("Files:\n")
print(files, end = "\n\n")
#==================================================
print("=================================\n")
#==================================================
all = vsechtoest(path)
print("Vse papki i files:\n")
print(all)