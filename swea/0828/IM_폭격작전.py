for test in range(1, int(input())+1):
    N, B = map(int, input().split())
    bomb = [list(map(int, input().split())) for _ in range(N)]
    arr = [[0]*N for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    sum_v = 0
    for _ in range(B):
        r, c, n = map(int, input().split())
        if arr[r][c] == 0:
            arr[r][c] = 1
            sum_v += bomb[r][c]
        for d in range(4):
            for i in range(1, n+1):
                tr, tc = r + dr[d] * i, c + dc[d] * i
                if 0 <= tr < N and 0 <= tc < N:
                    if arr[tr][tc] == 0:
                        arr[tr][tc] = 1
                        sum_v += bomb[tr][tc]
    print(f'#{test} {sum_v}')