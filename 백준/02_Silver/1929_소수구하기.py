M, N = list(map(int, input().split()))

arr = []
for i in range(M, N):
    for j in range(2, i):
        if i % j == 0:
            print(i)