def even_numbers_gen(n):
    for i in range(0, n+1, 2):
            yield i

n = int(input())

for num in even_numbers_gen(n):
    print(num)