import os

def dostup(path):
    info = {
        "existence": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),   
        "executable": os.access(path, os.X_OK)
    }
    return info

path = r"C:\Users\z3ske\Desktop\KBTU\PP2labs\lab6"

info = dostup(path)

print(f"Existence: {info['existence']}")
print(f"Readability: {info['readable']}")
print(f"Writability: {info['writable']}")
print(f"Executability: {info['executable']}")
