import sys;
from collections import deque

N = int(sys.stdin.readline())
Q = deque()

for _ in range(N):
    arr = list(sys.stdin.readline().split())
    if arr[0] == 'push_front':
        Q.appendleft(int(arr[1]))
    elif arr[0] == 'push_back':
        Q.append(int(arr[1]))
    elif arr[0] == 'pop_front':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif arr[0] == 'pop_back':
        if Q:
            print(Q.pop())
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