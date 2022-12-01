for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = 0
    for i in range(N - 1):
        cnt = 0
        for j in range(i + 1, N):
            if arr[i] <= arr[j]:
                cnt += 1
        if max_v < N - i - 1 - cnt:
            max_v = N - i - 1 - cnt
    print(f'#{TC}', max_v)