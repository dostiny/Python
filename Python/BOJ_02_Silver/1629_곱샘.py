def mul(a, b, c):
    if b == 1:
        return a % c

    if b % 2 == 0:
        return (mul(a, b // 2, c) ** 2) % c
    else:
        return ((mul(a, b // 2, c) ** 2) * a) % c

A, B, C = map(int, input().split())
print(mul(A, B, C))