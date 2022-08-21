import sys; sys.stdin = open('input/색칠하기_input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    area = [0] * N
    for i in range(N):
        area[i] = list(map(int, input().split()))
    arr = [[0]*10 for _ in range(10)]
    cnt = 0
    for j in range(N):
        sr, sc, er, ec, color = area[j][0], area[j][1], area[j][2], area[j][3], area[j][4]
        for r in range(sr, er+1):
            for c in range(sc, ec+1):

                if arr[r][c] == 0:
                    arr[r][c] = color
                elif arr[r][c] != 0:
                    arr[r][c] = 3
                    cnt +=1

    print(f'#{tc} {cnt}')