def count_upper_lower(str):
    upper = 0
    lower = 0

    for char in str:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return upper, lower

str = "Postavte full POZHALUYSTA APAY ~_~"
upper, lower = count_upper_lower(str)
print("Kishi :", upper)
print("Ulken :", lower)
