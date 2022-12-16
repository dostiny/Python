from collections import deque

def bfs():
    Q.append((0, 0))
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))


N, M = map(int, input().split())
arr = [list(map(int,input())) for _ in range(N)]
Q = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
bfs()

print(visited[N-1][M-1])