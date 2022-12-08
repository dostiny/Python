import sys;
from collections import deque

N = int(sys.stdin.readline())
Q = deque()
for i in range(N):
    Q.append(i + 1)

while len(Q) != 1:
    Q.popleft()
    a = Q.popleft()
    Q.append(a)

print(Q[0])