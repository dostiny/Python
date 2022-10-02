from collections import deque

def bfs(r, c, area):
    Q = deque()
    Q.append((r, c))
    visited[r][c] = 1

    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] >= area and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    Q.append((nr, nc))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = min(map(min, arr))
max_v = max(map(max, arr))
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

max_area = min_v
for area in range(min_v, max_v):
    visited = [[0] * N for _ in range(N)]
    temp = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] >= area and visited[r][c] == 0:
                bfs(r, c, area)
                temp += 1
    if max_area < temp:
        max_area = temp
print(max_area)