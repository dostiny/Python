import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while Q:
        r, c = Q.popleft()
        if r == y and c == x:
            return visited[r][c] - 1
        else:
            for i in range(8):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    Q.append((nr, nc))
    return 0

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(int(input())):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    Q = deque()
    r, c = map(int, input().split())
    y, x = map(int, input().split())
    Q.append((r, c))
    visited[r][c] = 1
    print(bfs())