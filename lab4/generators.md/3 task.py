def del_by_3_i_4_gen(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for num in del_by_3_i_4_gen(n):
    print(num)