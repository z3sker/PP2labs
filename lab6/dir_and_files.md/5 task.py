def func(file, info):
    with open(file, 'w') as file:
        for i in info:
            file.write(str(i) + '\n')

file = r'C:\Users\z3ske\Desktop\KBTU\PP2labs\lab6\file.txt'
info = ['postavte', 'poozhaluysta', 'full'] 

func(file, info)
print(f"massiv vstavlen v {file}")
