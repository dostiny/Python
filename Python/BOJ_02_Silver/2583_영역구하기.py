import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global cnt
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 0:
                Q.append((nr, nc))
                arr[nr][nc] = -1
                cnt += 1

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for i in range(x1, x2):
            arr[j][i] = 1
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
Q = deque()
cnt, ans = 0, []
for r in range(M):
    for c in range(N):
        if arr[r][c] == 0:
            arr[r][c] = -1
            cnt = 1
            Q.append((r, c))
            bfs()
            ans.append(cnt)
print(len(ans))
print(*sorted(ans))
