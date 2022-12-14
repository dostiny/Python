import sys;

N = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
stack = []
result = [0 for i in range(N)]

for i in range(N):
    while stack:
        if stack[-1][1] > top[i]:
            result[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, top[i]])

print(*result)

# 시간초과

# N = int(sys.stdin.readline())
# top = list(map(int, sys.stdin.readline().split()))
# arr = [0] * N
# max_n = 0
# for i in range(N-1, 0, -1):
#     for j in range(i - 1, 0, -1):
#         if top[i] < top[j]:
#             arr[i] = j + 1
#             break
# print(*arr)