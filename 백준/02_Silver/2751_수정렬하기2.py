n = int(input())
arr = sorted(list(set([int(input()) for _ in range(n)])))
for i in arr:
    print(i)