from collections import deque

def bfs():
    global cnt, zero_c
    while Q:
        cnt += 1
        n = len(Q)
        for _ in range(n):
            r, c = Q.popleft()
            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                    arr[nr][nc] = 1
                    zero_c -= 1
                    Q.append((nr, nc))
    if zero_c:
        cnt = -1

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
Q = deque()
cnt = -1
zero_c = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            Q.append((r, c))
        elif arr[r][c] == 0:
            zero_c += 1
bfs()
# for r in range(N):
#     for c in range(N):
#         if arr[r][c] == 0:
#             cnt = -1
#             break
print(cnt)