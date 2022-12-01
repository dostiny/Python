for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c, d, n = 0, 0, 0, 1
    while True:
        arr[r][c] = n
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r, c = nr, nc
            n += 1
        elif n == N ** 2:
            break
        else:
            d += 1
            d = d % 4
    print(f'#{TC}')
    for ar in arr:
        print(*ar)