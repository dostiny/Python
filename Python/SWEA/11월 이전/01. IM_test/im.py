'''
5
5 1 4
3 5 5 4 5
6 2 6
5 3 3 5 5 1
7 1 6
3 3 5 2 5 1 2
8 1 7
3 1 1 2 2 5 3 5
10 1 6
4 4 2 4 5 2 5 3 5 5
'''

for tc in range(1, int(input())+1):
    N, K_min, K_max = map(int, input().split())
    new = list(map(int, input().split()))
    new_li = list(set(new))
    new_li.sort()
    n = len(new_li)//2 + 1
    A = B = C = 0
    ans = 1001
    for i in range(1, n):
        for j in range(1, n):
            A = B = C = 0
            T1 = new_li[i]
            T2 = new_li[-j]
            if T1 >= T2:
                continue
            for k in new:
                if T2 <= k:
                    A += 1
                elif T1 <= k < T2:
                    B += 1
                elif k < T1:
                    C += 1
            max_v, min_v = max(A, B, C), min(A, B, C)
            if K_min <= min_v and max_v <= K_max:
                if ans >= max_v - min_v:
                    ans = max_v - min_v
    if ans == 1001:
        ans = -1
    print(f'#{tc} {ans}')
