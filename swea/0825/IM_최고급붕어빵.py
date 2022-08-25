# import sys; sys.stdin = open('input/IM_붕어빵_input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    bung = [0] * 11111
    for i in time:
        bung[i] += 1
    bung_cnt = 0
    for j in range(0, 11112, M):
        if j != 0:
            bung_cnt += K
            bung[j] -= bung_cnt

    print(bung)

