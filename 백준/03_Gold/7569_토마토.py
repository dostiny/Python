from collections import deque

def bfs():
    while Q:
        z, y, x = Q.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and arr[nz][ny][nx] == 0:
                arr[nz][ny][nx] = arr[z][y][x] + 1
                Q.append((nz, ny, nx))


M, N, H = map(int, input().split())
arr = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(H)]

Q = deque()
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for z in range(H):
    for y in range(N):
        for x in range(M):
            if arr[z][y][x] == 1:
                Q.append((z, y, x))
bfs()
bp = 0
result = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if arr[z][y][x] == 0:
                bp = -1
                break
            else:
                result = max(result, arr[z][y][x])
if bp == -1:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result - 1)