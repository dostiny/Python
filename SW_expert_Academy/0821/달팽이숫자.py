for tc in range(1, 4):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    dx = [0, 1, 0, -1] # 우 하 좌 상
    dy = [1, 0, -1, 0] # 우 하 좌 상
    r = c = 0
    d = 0    # 처음에는 무조건 우측방향이라서
    n = 1

    while True:
        arr[r][c] = n   # 0 0 에 1 입력 (현재위치)
        dr = r + dx[d]  # 우측으로 이동
        dc = c + dy[d]

        if 0 <= dr < N and 0 <= dc < N and arr[dr][dc] == 0:    # if 우측으로 이동했을때 범위
            r = dr
            c = dc
        else:   # 방향전환
            d = (d + 1) % 4
            r += dx[d]
            c += dy[d]

        if n == N**2:
            break

        n += 1

    print(*arr)