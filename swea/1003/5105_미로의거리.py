from collections import deque

def bfs():
    global cnt
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if 0 <= nr < N and 0 <= nc < N:
                if miro[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    Q.append((nr, nc))
                if miro[nr][nc] == 3:
                    visited[nr][nc] = visited[r][c]
                    return visited[nr][nc]
    return 0


for TC in range(1, int(input()) + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    Q = deque()
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]
    for r in range(N):
        for c in range(N):
            if miro[r][c] == 2:
                Q.append((r, c))
                break
    print(f'#{TC}', bfs())