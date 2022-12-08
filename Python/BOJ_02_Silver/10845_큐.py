import sys;
from collections import deque

N = int(sys.stdin.readline())
Q = deque()

for _ in range(N):
    arr = list(sys.stdin.readline().split())
    if arr[0] == 'push':
        Q.append(int(arr[1]))
    elif arr[0] == 'pop':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(Q))
    elif arr[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif arr[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)