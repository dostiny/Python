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
# n = 5
# light = [[[] for _ in range(n)] for _ in range(n)]
# print(light)


arr = [1, 3, 4, 5, 6, 2, 4, 8, 1, 5, 8, 7, 3, 4, 1, 6, 3, 4, 2, 8, 1, 4, 4, 8, 7, 5, 2, 8, 8, 1, 1, 7, 6, 2, 8, 4, 4, 5, 5, 1, 4, 7, 6, 7, 4, 7, 2, 7, 5, 5, 5, 8, 3, 4, 8, 3, 2, 7, 5, 1, 2, 7, 4, 3]
dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
acnt = bcnt = 0

for i in arr:
    dict[i] += 1
    if i <= 4:
        acnt += 1
    else:
        bcnt += 1

for key, value in dict.items():
    print(f'{key}반 : {value}명')
print(f'비전공 {acnt + dict[4]}명 vs 전공 {bcnt - dict[4]}명')
print(f'파이썬 {acnt}명 vs 자바 {bcnt}명')
print(f'총 {acnt + bcnt}명')
