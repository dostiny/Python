for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v, min_v = 0, 100000000
    for i in range(N):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]
    print(f'#{TC}', max_v - min_v)