# visited = [0] * 30
# for i in range(28):
#     n = int(input())
#     visited[n - 1] = 1
# for j in range(30):
#     if visited[j] == 0:
#         print(j + 1)

# numli = []
# while True:
#     N, M = map(int, input().split())
#     if N == 0 and M == 0:
#         break
#     else:
#         numli.append((N, M))
# for N, M in numli:
#     if N > M:
#         print("Yes")
#     else:
#         print("No")

# import sys;
#
# arr = list(map(int, sys.stdin.readline().split()))
# print(arr)

# from collections import deque
#
# q = deque()
# ww = (1, 2)
# q.append((1, 2))
# q.append((2, 3))
# if ww in q:
#     print(1)
n = 5
light = [[[] for _ in range(n)] for _ in range(n)]
print(light)