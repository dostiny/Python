N = int(input())

result = 0
for i in range(1, N + 1):
    A = list(map(int, str(i)))
    result = i + sum(A)
    if N == result:
        print(i)
        break
    if N == i:
        print(0)