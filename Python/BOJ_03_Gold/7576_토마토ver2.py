from collections import deque

def bfs():
    global cnt, result
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                cnt -= 1
                if result < visited[nr][nc]:
                    result = visited[nr][nc]
                Q.append((nr, nc))

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
Q = deque()
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = result = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            Q.append((r, c))
        elif arr[r][c] == 0:
            cnt += 1
bfs()
# for ar in visited:
#     print(ar)
# print(result, cnt)
if cnt:
    print(-1)
else:
    print(result)