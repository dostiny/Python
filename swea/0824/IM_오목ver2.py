import sys; sys.stdin = open('input/IM_오목_input.txt', 'r')
# 'o'
for tc in range(1, int(input())+1):
    N = int(input())
    ohm = [list(map(str, input())) for _ in range(N)]
    result = 'NO'

    for r in range(N - 4):
        for c in range(N - 4):
            for y in range(5):              # 가로
                cnt_1 = 0
                for x in range(5):
                    if ohm[r+y][c+x] == 'o':
                        cnt_1 += 1
                        if cnt_1 == 5:
                            result = 'YES'

            for x in range(5):              # 세로
                cnt_2 = 0
                for y in range(5):
                    if ohm[r+y][c+x] == 'o':
                        cnt_2 += 1
                        if cnt_2 == 5:
                            result = 'YES'

            cnt_3 = 0
            for i in range(5):              # 우하행
                if ohm[r+i][c+i] == 'o':
                    cnt_3 += 1
                    if cnt_3 == 5:
                        result = 'YES'

            cnt_4 = 0
            for j in range(5):              # 좌하행
                if ohm[r+j][c+4-j] == 'o':
                    cnt_4 += 1
                    if cnt_4 == 5:
                        result = 'YES'


    print(f'#{tc} {result}')

