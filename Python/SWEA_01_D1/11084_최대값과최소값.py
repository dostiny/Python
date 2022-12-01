for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v, max_idx = 0, 0
    min_v, min_idx = N, 11
    for i in range(N):
        if max_v <= arr[i]:
            max_v = arr[i]
            max_idx = i
        if min_v > arr[i]:
            min_v = arr[i]
            min_idx = i
    print(f'#{TC}', abs(max_idx - min_idx))