import re

pattern = "[A-Z]{1}[a-z]+"

test_strings = ["Hello", "World", "PythonProgram", "Kbtu", "KBTU", 
                
                "Postave full please"]

for test in test_strings:
    x = re.findall(pattern, test)
    print(test, end=' ')
    if x:
        print("MATCHES the pattern\n")
    else:
        print("DOES NOT match the pattern\n")