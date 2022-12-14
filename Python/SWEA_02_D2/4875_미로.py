from collections import deque
for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    Q = deque()
    result = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                Q.append((r, c))
    while Q:
        r, c = Q.popleft()
        visited[r][c] = 1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N  and visited[nr][nc] == 0 and arr[nr][nc] == 0:
                Q.append((nr, nc))
            elif 0 <= nr < N and 0 <= nc < N  and arr[nr][nc] == 3:
                result = 1
    print(f'#{TC}', result)