T = int(input())

for i in range(1, T+1):
    x, y = map(int, input().split())
    print(f'#{i}', end=' ')
    if x < y:
        print('<')
    elif x > y:
        print('>')
    elif x == y:
        print('=')