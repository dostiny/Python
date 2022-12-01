from collections import deque

def bfs(yesno, color):
    if yesno == 1:
        while Q:
            r, c = Q.popleft()
            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == color and not yesrgb[nr][nc]:
                    yesrgb[nr][nc] = 1
                    Q.append((nr, nc))
    elif yesno == 2:
        if color == 'R' or color == 'G':
            while Q:
                r, c = Q.popleft()
                for i in range(4):
                    nr, nc = r + dy[i], c + dx[i]
                    if 0 <= nr < N and 0 <= nc < N and not norgb[nr][nc] and (arr[nr][nc] == 'R' or arr[nr][nc] == 'G'):
                        norgb[nr][nc] = 1
                        Q.append((nr, nc))
        else:
            while Q:
                r, c = Q.popleft()
                for i in range(4):
                    nr, nc = r + dy[i], c + dx[i]
                    if 0 <= nr < N and 0 <= nc < N and not norgb[nr][nc] and arr[nr][nc] == color:
                        norgb[nr][nc] = 1
                        Q.append((nr, nc))

N = int(input())
arr = [list(input()) for _ in range(N)]
yesrgb = [[0] * N for _ in range(N)]
norgb = [[0] * N for _ in range(N)]
Q = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
ans1, ans2 = 0, 0
for r in range(N):
    for c in range(N):
        if not yesrgb[r][c]:
            ans1 += 1
            color = arr[r][c]
            Q.append((r, c))
            yesrgb[r][c] = 1
            bfs(1, color)
        if not norgb[r][c]:
            ans2 += 1
            color = arr[r][c]
            Q.append((r, c))
            norgb[r][c] = 1
            bfs(2, color)
print(ans1, ans2)