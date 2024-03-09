import re

pattern = "a.*b"

test_strings = ["acb", "ax", "efwqeq", "a123b", "axb", "ab", "a1b", "a b", "abc",  
                
                "Postave full please"]

for test in test_strings:
    x = re.fullmatch(pattern, test)
    print(test, end=' ')
    if x:
        print("MATCHES the pattern\n")
    else:
        print("DOES NOT match the pattern\n")