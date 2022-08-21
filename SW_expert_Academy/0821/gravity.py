for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    height = 0
    max_v = 0
    for i in range(N):
        cnt = 0
        for j in arr:
            if arr[i] <= j:
                cnt += 1
        height = N - i - cnt
        if max_v < height:
            max_v = height
    print(f'#{tc} {max_v}')
