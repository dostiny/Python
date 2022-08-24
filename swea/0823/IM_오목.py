import sys; sys.stdin = open('input/IM_오목_input.txt', 'r')
# 'o'
for tc in range(1, int(input())+1):
    N = int(input())
    ohm = [list(map(str, input())) for _ in range(N)]
    yes_li = []
    for r in range(N):
        cnt_1 = cnt_2 = cnt_3 = cnt_4 = 0
        for c in range(N):
            if ohm[r][c] == 'o':
                cnt_1 += 1
            if ohm[c][r] == 'o':
                cnt_2 += 1
            if ohm[c][c] == 'o':
                cnt_3 += 1
            if ohm[c][N-1-c] == 'o':
                cnt_4 += 1
        if cnt_1 == 5 or cnt_2 == 5 or cnt_3 == 5 or cnt_4 == 5:
            result = 'YES'
            break
    else:
        result = 'NO'
    print(f'#{tc} {result}')
