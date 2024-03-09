import re

do = "Nadezhda umiraet Poslednei Deidi goj"

posle = re.findall('[A-Z][^A-Z]*', do)

print("Do   :", do)
print("Posle:", posle)