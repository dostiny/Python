t = int(input())

for _ in range(t):
    n, s = input().split()
    n = int(n)
    for i in s:
        print(i * n, end='')
    print('')