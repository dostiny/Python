

for test_case in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    square = [[0] * 10 for _ in range(10)]
    cnt = 0
    for i in arr:
        r1, c1 = i[0], i[1]
        r2, c2 = i[2], i[3]
        rh = r2 - r1
        ch = c2 - c1
        color = i[4]

        for x in range(r1, r1+rh+1):
            for y in range(c1, c1+ch+1):
                if square[x][y] == 0:
                    square[x][y] = color
                elif square[x][y] != 0:
                    square[x][y] = 3
                    cnt += 1
    for i in square:
        print(i)
    print(f'#{test_case} {cnt}')