N = int(input())

arr = [['*'] * N for _ in range(N)]

for i in arr:
    print(*i)