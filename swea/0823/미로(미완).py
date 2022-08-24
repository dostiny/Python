import sys; sys.stdin = open('input/미로_input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                sc, sr = c, r
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    c_point = []
    go = []
    while True:
        cnt = 0
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 범위 제한
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
                if arr[nr][nc] == 0:
                    cnt += 1
                    go = [r, c, d]
                if cnt > 1:
                    c_point.append(go)