import re

pattern = "ab{2,3}"

test_strings = ["ac", "abc", "abbc", "a", "abb", "sdqde", "bbde", 
                
                "Postave full please"]

for test in test_strings:
    x = re.match(pattern, test)
    print(test, end=' ')
    if x:
        print("MATCHES the pattern\n")
    else:
        print("DOES NOT match the pattern\n")