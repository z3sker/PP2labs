import re

pattern = "[a-z]+_[a-z]+"

test_strings = ["hello_worldd", "python_program", "KBTU", "kbtu_BACHELOR",
                
                "Postave full please"]

for test in test_strings:
    x = re.findall(pattern, test)
    print(test, end=' ')
    if x:
        print("MATCHES the pattern\n")
    else:
        print("DOES NOT match the pattern\n")