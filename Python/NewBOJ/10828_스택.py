import sys

input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    order = list(input().split())
    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if len(stack):
            n = stack.pop()
        else:
            n = -1
        print(n)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack):
            n = 0
        else:
            n = 1
        print(n)
    else:
        if len(stack):
            n = stack[-1]
        else:
            n = -1
        print(n)