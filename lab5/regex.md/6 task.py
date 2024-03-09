import re

pattern = "[ ,.]"

do = "Mozhete postavit full, pozhaluysta."

posle = re.sub(pattern, ":", do)

print("Do   :", do)
print("Posle:", posle)