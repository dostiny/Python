import sys
from collections import deque

input = sys.stdin.readline

dqe = deque()

N = int(input())

for _ in range(N):
    order = list(input().split())
    if order[0] == 'push_front':
        dqe.appendleft(int(order[1]))
    elif order[0] == 'push_back':
        dqe.append(int(order[1]))
    elif order[0] == 'pop_front':
        if len(dqe):
            print(dqe.popleft())
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if len(dqe):
            print(dqe.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(dqe))
    elif order[0] == 'empty':
        if len(dqe):
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if len(dqe):
            print(dqe[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(dqe):
            print(dqe[-1])
        else:
            print(-1)