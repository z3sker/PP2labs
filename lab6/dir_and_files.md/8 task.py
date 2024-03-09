import os

def func(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File v {path} byl udalen")
        else:
            print(f"net dostupa k {path}.")
    else:
        print(f"{path} takogo puti netu")

path = r'C:\Users\z3ske\Desktop\KBTU\PP2labs\lab6\file.txt'

func(path)
