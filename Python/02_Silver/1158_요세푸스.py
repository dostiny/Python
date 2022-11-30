import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
Q = deque([i for i in range(1, N + 1)])
ans = []
cnt = 0
print('<', end='')
while len(Q) != 1:
    cnt += 1
    a = Q.popleft()
    if cnt % K == 0:
        print(a, end=', ')
    else:
        Q.append(a)
print(f'{Q[0]}>')