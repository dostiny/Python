def backtrack(k, sum_v):
    global cnt;
    if k == N:
        # print(pick)
        if sum_v == K:
            cnt += 1
        return
    else:
        pick.append(arr[k])
        backtrack(k + 1, sum_v + arr[k])
        # print('--')
        pick.pop()
        backtrack(k + 1, sum_v)
        # print('==')

for TC in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    pick = []
    backtrack(0, 0)
    print(f'#{TC}', cnt)