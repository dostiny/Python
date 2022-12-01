for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    print(f'#{TC}', *arr)