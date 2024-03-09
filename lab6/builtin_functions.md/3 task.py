def palindrome(s):
    rs = s[::-1]
    return s == rs

s1, s2 = "sps", "apai"
if palindrome(s1):
    print("palindrome")
else:
    print("ne palindrome")