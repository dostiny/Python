for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    r, c, d, n = 0, 0, 0, 1
    while True:
        arr[r][c] = n
        nr, nc = r + dy[d], c + dx[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r, c = nr, nc
            n += 1
        elif n == N*N:
            break
        else:
            d = (d + 1) % 4
    print(f'#{TC}')
    for ar in arr:
        print(*ar)