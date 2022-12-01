for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    place = [[0] * N for _ in range(N)]
    bomb = [list(map(int, input().split())) for _ in range(B)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    sum_v = 0
    for b in bomb:
        r, c, n = b[0], b[1], b[2]
        if place[r][c] == 0:
            sum_v += arr[r][c]
            place[r][c] = 1
        for d in range(4):
            for i in range(1, 1 + n):
                nr, nc = r + dr[d] * i, c + dc[d] * i
                if 0 <= nr < N and 0 <= nc < N:
                    if place[nr][nc] == 0:
                        place[nr][nc] = 1
                        sum_v += arr[nr][nc]

    print(f'#{tc} {sum_v}')