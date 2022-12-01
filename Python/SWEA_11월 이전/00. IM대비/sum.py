import sys; sys.stdin = open('input/sum_input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_v = 0

    # 가로 합
    for r in range(100):
        sum_v = 0
        for c in range(100):
            sum_v += arr[r][c]
        if max_v < sum_v:
            max_v = sum_v

    # 세로 합
    for c in range(100):
        sum_v = 0
        for r in range(100):
            sum_v += arr[r][c]
        if max_v < sum_v:
            max_v = sum_v

    # 대각선 합 (남동)
    sum_v = 0
    for rc in range(100):
        sum_v += arr[rc][rc]
    if max_v < sum_v:
        max_v = sum_v

    # 대각선 합 (남서)
    sum_v = 0
    for rc in range(100):
        sum_v += arr[rc][99-rc]
    if max_v < sum_v:
        max_v = sum_v

    print(f'#{tc} {max_v}')