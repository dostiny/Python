import sys; sys.stdin = open('input/IM_오목_input.txt', 'r')
# 'o'
for tc in range(1, int(input())+1):
    N = int(input())
    ohm = [list(map(str, input())) for _ in range(N)]
    result = 0
    for r in range(N):      # 가로
        cnt_1 = 0
        for c in range(N):
            if ohm[r][c] == 'o':
                cnt_1 += 1
                if cnt_1 == 5:
                    result = 'YES'
                    break
            else:
                break
        if result == 'YES':
            break

    for c in range(N):      # 세로
        cnt_2 = 0
        for r in range(N):
            if ohm[r][c] == 'o':
                cnt_2 += 1
                if cnt_2 == 5:
                    result = 'YES'
                    break
            else:
                break
        if result == 'YES':
            break


    for r in range(N-4):    # 우하행 대각
        for c in range(N-4):
            cnt_3 = 0
            for i in range(5):
                if ohm[r+i][c+i] == 'o':
                    cnt_3 += 1
                    if cnt_3 == 5:
                        result = 'YES'
                        break
                else:
                    break
            if result == 'YES':
                break


    for r in range(N-4):    # 좌하행 대각
        for c in range(N-1, 3, -1):
            cnt_4 = 0
            for i in range(5):
                if ohm[r+i][c-i] == 'o':
                    cnt_4 += 1
                    if cnt_4 == 5:
                        result = 'YES'
                        break
                else:
                    break
            if result == 'YES':
                break

    if result != 'YES':
        result = 'NO'


    print(f'#{tc} {result}')