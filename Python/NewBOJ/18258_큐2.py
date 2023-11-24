import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
deq = deque()

for _ in range(N):
    arr = list(input().split())
    if arr[0] == 'push':
        deq.append(int(arr[1]))
    elif arr[0] == 'pop':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(deq))
    elif arr[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif arr[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)