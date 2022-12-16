from collections import deque

def bfs():
    global cnt, big_p
    pcnt = 0
    cnt += 1
    while Q:
        r, c = Q.popleft()
        if arr[r][c] == 1:
            pcnt += 1
            arr[r][c] = -1
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1:
                    Q.append((nr, nc))
    if big_p < pcnt:
        big_p = pcnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = big_p = 0
Q = deque()
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for r in range(n):
    for c in range(m):
        if arr[r][c] == 1:
            Q.append((r, c))
            bfs()
print(cnt)
print(big_p)