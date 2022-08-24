import sys; sys.stdin = open('미로_input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    S = []
    dr = [1, -1, 0, 0] # 하 상 우 좌
    dc = [0, 0, 1, -1]
    # 시작점을 찾는다.
    r = c = er = ec = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j
            elif maze[i][j] == 3:
                er, ec = i, j
    # 시작점을 방문하고, 스택에 push
    S = [(r, c)]
    visited[r][c] = 0

    # 빈스택이 아닐동안 반복
    while S:
        for i in range(4):  # (r, c) 의 상하좌우 인접한 곳의 좌표를 생성
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc <0 or nc >= N:
                continue
            if maze[nr][nc] != 1 and visited[nr][nc] == 0:  # 벽이거나 방문했거나
                S.append((r, c))
                visited[nr][nc] = 1
                r, c = nr, nc
                break
            else:
                r, c = S.pop()
        print(visited[er][ec])
