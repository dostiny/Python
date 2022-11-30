N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
result = sorted(arr, key = lambda x: (x[1], x[0]))
for a, b in result:
    print(a, b)