for TC in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_v, min_v = 0, 99999999
    for i in range(N - M + 1):
        sum_v = 0
        for j in range(M):
            sum_v += arr[i + j]
        if max_v < sum_v:
            max_v = sum_v
        if min_v > sum_v:
            min_v = sum_v
    print(max_v - min_v)