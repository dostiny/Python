# def ans(s):
#     global cnt
#     if sum(pick) == K:
#         cnt += 1
#         return
#     elif sum(pick) > K:
#         return
#
#     for i in range(s, N):
#         if visited[i] == 0:
#             pick.append(arr[i])
#             visited[i] = 1
#             ans(i+1)
#             pick.pop()
#             visited[i] = 0
#
# for TC in range(1, int(input()) + 1):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#     visited = [0] * N
#     pick = []
#     cnt = 0
#     ans(0)
#     print(f'#{TC}', cnt)

#================================================

def ans(s, sum_v):
    global cnt
    if sum_v == K:
        cnt += 1
        return
    elif sum_v > K:
        return
    else:
        for i in  range(s, N):
            if visited[i] == 0:
                visited[i] = 1
                ans(i, sum_v + arr[i])
                visited[i] = 0

for TC in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * N
    cnt = 0
    ans(0, 0)
    print(f'#{TC}', cnt)