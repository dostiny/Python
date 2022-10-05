def backtrack(k, cur_sum):
    global cnt
    # if cur_sum > K:
    #     return
    # if k == N:
    #     if cur_sum == K:
    #         cnt += 1
    if k == N:
        print(pick)
    else:
        pick.append(arr[k])
        print(k)
        backtrack(k + 1, cur_sum + arr[k])
        pick.pop()
        backtrack(k + 1, cur_sum)

for TC in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = list(map(int,input().split()))
    cnt = 0
    pick = []
    backtrack(0, 0)
    print(f'#{TC}', cnt)