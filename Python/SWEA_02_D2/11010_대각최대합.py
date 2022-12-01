for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 1, 1, -1]
    dc = [1, 1, -1, -1]
    result = 0
    for r in range(N):
        for c in range(N):
            sum_v = arr[r][c]
            for i in range(4):
                for j in range(1, N):
                    nr = r + dr[i] * j
                    nc = c + dc[i] * j
                    if 0 <= nr < N and 0 <= nc < N:
                        sum_v += arr[nr][nc]
            if result < sum_v:
                result = sum_v
    print(f'#{TC}', result)