from collections import deque

def bfs():
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                arr[nr][nc] = 0
                Q.append((nr, nc))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    Q = deque()
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                cnt += 1
                arr[r][c] = 0
                Q.append((r, c))
                bfs()

    print(cnt)