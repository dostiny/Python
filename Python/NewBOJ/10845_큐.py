import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

deq = deque()

for _ in range(N):
    order = list(input().split())
    if order[0] == 'push':
        deq.append(order[1])
    elif order[0] == 'pop':
        if len(deq):
            n = deq.popleft()
            print(n)
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(deq))
    elif order[0] == 'empty':
        if len(deq):
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if len(deq):
            print(deq[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(deq):
            print(deq[-1])
        else:
            print(-1)