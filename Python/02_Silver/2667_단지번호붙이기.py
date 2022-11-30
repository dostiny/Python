# =========================================
# DFS

# def dfs(r, c):
#     if r < 0 or N <= r or c < 0 or N <= c:
#         return
#     if arr[r][c] == 1:
#         result[-1] += 1
#         arr[r][c] = 0
#         dfs(r + 1, c)
#         dfs(r - 1, c)
#         dfs(r, c + 1)
#         dfs(r, c - 1)
#     return
#
# N = int(input())
# arr = [list(map(int, input())) for _ in range(N)]
# result = [0]
# for y in range(N):
#     for x in range(N):
#         if arr[y][x] == 0:
#             continue
#         elif arr[y][x] == 1:
#             result[0] += 1
#             result.append(0)
#             dfs(y, x)
# print(result[0])
# for i in sorted(result[1:]):
#     print(i)

# =========================================
# BFS

from collections import deque

def bfs():
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
                result[-1] += 1
                arr[nr][nc] = 0
                queue.append([nr, nc])

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
queue = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
cnt, result = 0, []
for y in range(N):
    for x in range(N):
        if arr[y][x] == 1:
            arr[y][x] = 0
            cnt += 1
            result.append(1)
            queue.append([y, x])
            bfs()
print(cnt)
for i in sorted(result):
    print(i)