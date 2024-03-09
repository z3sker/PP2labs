import re

def spaces(str):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str)

s1 = "YaBylByRadBuyrsta"
s2 = "Podumaitepozhalusta"
print(spaces(s1))
print(spaces(s2))