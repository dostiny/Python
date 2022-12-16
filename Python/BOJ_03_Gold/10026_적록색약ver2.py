import sys
from collections import deque
input = sys.stdin.readline

def normal(st):
    while normalQ:
        r, c = normalQ.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == st and normal_vi[nr][nc] == 0:
                normal_vi[nr][nc] = 1
                normalQ.append((nr, nc))

def rgb(st):
    while rgbQ:
        r, c = rgbQ.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and rgb_vi[nr][nc] == 0:
                if (st == "B" and arr[nr][nc] == "B"):
                    rgb_vi[nr][nc] = 1
                    rgbQ.append((nr, nc))
                elif (st == "R" or st == "G") and (arr[nr][nc] == "R" or arr[nr][nc] == "G"):
                    rgb_vi[nr][nc] = 2
                    rgbQ.append((nr, nc))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = int(input())
arr = [list(input().rstrip('\n')) for _ in range(N)]
normalQ, rgbQ = deque(), deque()
normal_vi = [[0] * N for _ in range(N)]
rgb_vi = [[0] * N for _ in range(N)]
nocnt = rgbcnt = 0

for r in range(N):
    for c in range(N):
        if normal_vi[r][c] == 0:
            # print(f'normal-> {r, c}')
            nocnt += 1
            normal_vi[r][c] = 1
            normalQ.append((r, c))
            normal(arr[r][c])
        if rgb_vi[r][c] == 0:
            # print(f'rgb-> {r, c}')
            rgbcnt += 1
            rgb_vi[r][c] = 1
            rgbQ.append((r, c))
            rgb(arr[r][c])

print(nocnt, rgbcnt)