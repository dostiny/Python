def thtn(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return n

a, b = map(int, input().split())
cnt = 0

for i in range(a, b+1):
    cnt += thtn(i)

print(cnt)