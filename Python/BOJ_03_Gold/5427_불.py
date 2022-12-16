import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while FI:
        y, x = FI.popleft()
        for i in range(4):
            ny, nx = y + dr[i], x + dc[i]
            if 0 <= ny < R and 0 <= nx < C and Fvisited[ny][nx] == 0 and arr[ny][nx] != "#":
                Fvisited[ny][nx] = Fvisited[y][x] + 1
                FI.append((ny, nx))

    while JI:
        r, c = JI.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if Jvisited[nr][nc] == 0 and arr[nr][nc] == '.':
                    if Fvisited[nr][nc] == 0 or Fvisited[nr][nc] > Jvisited[r][c] + 2:
                        Jvisited[nr][nc] = Jvisited[r][c] + 1
                        JI.append((nr, nc))
            else:
                return Jvisited[r][c] + 1

    return "IMPOSSIBLE"

for _ in range(int(input())):
    C, R = map(int, input().split())
    arr = [list(input().rstrip('\n')) for _ in range(R)]
    JI, FI = deque(), deque()
    Jvisited = [[0] * C for _ in range(R)]
    Fvisited = [[0] * C for _ in range(R)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for j in range(R):
        for i in range(C):
            if arr[j][i] == "@":
                JI.append((j, i))
            elif arr[j][i] == "*":
                Fvisited[j][i] = 1
                FI.append((j, i))
    print(bfs())