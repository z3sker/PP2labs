from math import tan, pi

sides = 4
length = 25

area = int(sides * (length ** 2) / (4 * tan(pi / sides)))

print(area)
