# import sys; sys.stdin = open('input/IM_붕어빵_input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    peo = list(map(int, input().split()))

    bung_cnt = 0
    result = 'Possible'
    for j in range(0, 11111):
        if j == 0:
            if j in peo:
                result = 'Impossible'
                break
        else:
            if j % M == 0:
                bung_cnt += K
            if j in peo:
                cnt = peo.count(j)
                bung_cnt -= cnt
            if bung_cnt < 0:
                result = 'Impossible'
                break

    print(f'#{tc} {result}')