import sys; sys.stdin = open('input_미로.txt')
from collections import deque

# def bfs(y, x):
#     global result
#     queue = deque()
#     queue.append((y, x))
#
#     while queue:
#         r, c = queue.popleft()
#         for i in range(4):
#             tr, tc = r + dy[i], c + dx[i]
#             if 0 <= tr < N and 0 <= tc < N and arr[tr][tc] == 0:
#                 arr[r][c] = -1
#                 queue.append((tr, tc))
#             elif 0 <= tr < N and 0 <= tc < N and arr[tr][tc] == 3:
#                 result = 1
#                 return



for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    queue = deque()
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]
    result = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                queue.append((r, c))

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            tr, tc = y + dy[i], x + dx[i]
            if 0 <= tr < N and 0 <= tc < N and arr[tr][tc] == 0:
                arr[y][x] = -1
                queue.append((tr, tc))
            elif 0 <= tr < N and 0 <= tc < N and arr[tr][tc] == 3:
                result = 1
                break
    print(f'#{TC} {result}')