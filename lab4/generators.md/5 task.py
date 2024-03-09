def dokonca(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for num in dokonca(n):
    print(num)