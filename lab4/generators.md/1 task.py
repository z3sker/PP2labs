def square_generator(N):
    for i in range(1, N):
        yield i**2

N = int(input())
for square in square_generator(N+1):
    print(square)
