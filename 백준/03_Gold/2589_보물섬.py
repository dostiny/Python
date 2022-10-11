from collections import deque

def bfs():
    global cnt
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < L and 0 <= nc < W and arr[nr][nc] == 'L' and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                cnt = visited[nr][nc]
                Q.append((nr, nc))

L, W = map(int, input().split())
arr = [list(input()) for _ in range(L)]
Q = deque()
cnt = ans = 0
for r in range(L):
    for c in range(W):
        visited = [[0] * W for _ in range(L)]
        if arr[r][c] == 'L':
            Q.append((r, c))
            visited[r][c] = 1
            bfs()
            if ans < cnt:
                ans = cnt

print(ans-1)
