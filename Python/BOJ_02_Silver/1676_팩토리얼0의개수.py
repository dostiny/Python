def factori(n):
    if n > 1:
        return n * factori(n - 1)
    else:
        return 1
N = int(input())
num = factori(N)
cnt, d = 0, 10
while True:
    if num % d == 0:
        cnt += 1
        d *= 10
    else:
        break
print(cnt)