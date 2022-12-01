for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = 0
    for i in range(N - 1):
        if max_v < arr[i] + arr[i + 1]:
            max_v = arr[i] + arr[i + 1]
    print(f'#{TC}', max_v)
