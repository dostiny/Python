import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    cnt = 0
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                Q.append((nr, nc))
    return cnt

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = int(input())
arr = [list(map(int, input().rstrip("\n"))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
Q = deque()
cnt = 0
danji = [0]

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1 and visited[r][c] == 0:
            cnt += 1
            danji.append(1)
            Q.append((r, c))
            visited[r][c] = 1
            danji[cnt] += bfs()

print(cnt)
for ans in sorted(danji):
    if ans != 0:
        print(ans)