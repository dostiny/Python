import sys; sys.stdin = open('input/IM_파리_input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            sum_v = 0
            for y in range(M):
                for x in range(M):
                    sum_v += fly[r+y][c+x]
            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')
