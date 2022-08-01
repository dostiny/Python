T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    print(f'#{i}', end=' ')
    print(a // b, end=' ')
    print(a % b)