for _ in range(1, 11):
    TC = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_v = 0
    # 가로
    for r in range(100):
        sum_v = 0
        for c in range(100):
            sum_v += arr[r][c]
        if max_v < sum_v:
            max_v = sum_v
    # 세로
    for c in range(100):
        sum_v = 0
        for r in range(100):
            sum_v += arr[r][c]
        if max_v < sum_v:
            max_v = sum_v
    # 우하
    r, c, sum_v = 0, 0, 0
    for i in range(100):
        nr, nc = r + i, c + i
        if 0 <= nr < 100 and 0 <= nc < 100:
            sum_v += arr[nr][nc]
    if max_v < sum_v:
        max_v = sum_v
    # 좌하
    r, c, sum_v = 0, 99, 0
    for i in range(100):
        nr, nc = r + i, c - i
        if 0 <= nr < 100 and 0 <= nc < 100:
            sum_v += arr[nr][nc]
    if max_v < sum_v:
        max_v = sum_v

    print(f'#{TC}', max_v)
