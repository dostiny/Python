import sys
from collections import deque
# input = sys.stdin.readline

def count():
    global cnt


def bfs():
    pass

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
Q, B = deque(), deque()
for r in range(N):
    for c in range(M):
        if arr[r][c] != 0:
            cnt += 1
            bfs()