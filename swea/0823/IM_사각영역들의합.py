import sys; sys.stdin = open('input/IM_사각_input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    zero_arr = [[0]*N for _ in range(N)]
    result = 0
    for _ in range(M):
        y, x, a = map(int, input().split())
        if y + a > N:
            ny = N
        else:
            ny = y + a
        if x + a > N:
            nx = N
        else:
            nx = x + a
        for r in range(y, ny):
            for c in range(x, nx):
                zero_arr[r][c] = 1
    for r in range(N):
        for c in range(N):
            if zero_arr[r][c] == 1:
                result += arr[r][c]

    print(f'#{tc} {result}')