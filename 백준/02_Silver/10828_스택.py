# N = int(input())
#
# stack = []
# for _ in range(N):
#     # print(f'---------{stack}----------')
#     arr = input().split()
#     if arr[0] == 'push':
#         stack.append(int(arr[1]))
#     elif arr[0] == 'pop':
#         if len(stack):
#             p = stack.pop()
#             print(p)
#         else:
#             print(-1)
#     elif arr[0] == 'size':
#         print(len(stack))
#     elif arr[0] == 'empty':
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
#     elif arr[0] == 'top':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[-1])


# ==================================================

import sys
n = int(sys.stdin.readline())

stack = []
for i in range(n):
    arr = sys.stdin.readline().split()

    if arr[0] == 'push':
        stack.append(int(arr[1]))
    elif arr[0] == 'pop':
        if len(stack):
            p = stack.pop()
            print(p)
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(stack))
    elif arr[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])