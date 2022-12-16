import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    Q.append((0, 0))
    visited[0][0] = 1
    arr[0][0] = 1
    for r, c in light[0][0]:
        arr[r][c] = 1

    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] == 1:
                visited[nr][nc] = 1
                Q.append((nr, nc))
                for y, x in light[nr][nc]:
                    arr[y][x] = 1

                    for j in range(4):
                        mr, mc = y + dr[j], x + dc[j]
                        if 0 <= mr < N and 0 <= mc < N and arr[mr][mc] == 1 and visited[mr][mc] == 1:
                            Q.append((mr, mc))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
arr = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
light = [[[] for _ in range(N)] for _ in range(N)]
Q = deque()
cnt = 0

for _ in range(M):
    y, x, b, a = map(int, input().split())
    y, x, b, a = y - 1, x - 1, b - 1, a - 1
    light[y][x].append((b, a))

bfs()

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            cnt += 1
print(cnt)