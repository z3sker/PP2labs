from functools import reduce

def multiply(numbers):
    res = reduce(lambda x, y: x * y, numbers)
    return res

numbers = [1, 2, 3, 4, 5]
res = multiply(numbers)
print(res)
