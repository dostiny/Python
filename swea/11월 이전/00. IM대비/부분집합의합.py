# for tc in range(1, int(input())+1):
#     N, K = map(int, input().split())
#     cnt = 0
#     arr = []
#     cnt = 0
#     for i in range(1, 13):
#         if K - i > 0:
#             K -= i
#             cnt += 1
#             arr.append(i)
#         elif K - i == 0:
#             K -= i
#             cnt += 1
#             arr.append(i)
#             break
#         elif K - i < 0:
#             pass
#
#     if cnt == N and K == 0:
#         result = 1
#     else:
#         result = 0
#     print(arr)
#     print(f'#{tc} {result}')

T = int(input())
for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = range(1, 13)
    count = 0
    for i in range(1 << 12):
        li = []
        for j in range(12):
            if i & (1 << j):
                li.append(arr[j])
        if len(li) == N:
            if sum(li) == K:
                count += 1
    print(f'#{test_case} {count}')
