from collections import deque

for _ in range(1, 11):
    TC = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    y, x = 99, 0
    for i in range(100):
        if arr[99][i] == 2:
            x = i
    dr = [-1, 0, 0]
    dc = [0, 1, -1]
    Q = deque()
    Q.append((y, x))
    result = 0
    while Q:
        r, c = Q.popleft()
        if r == 0:
            result = c
            break
        # 상
        tr, tc = r + dr[0], c + dc[0]
        # 우
        rr, rc = r + dr[1], c + dc[1]
        # 좌
        lr, lc = r + dr[2], c + dc[2]
        arr[r][c] = 2
        if arr[tr][tc] == 1:
            if 0 <= rc < 100 and arr[rr][rc] == 1:
                Q.append((rr, rc))
            elif 0 <= lc < 100 and arr[lr][lc] == 1:
                Q.append((lr, lc))
            else:
                Q.append((tr, tc))
        elif arr[tr][tc] == 0:
            if 0 <= rc < 100 and arr[rr][rc] == 1:
                Q.append((rr, rc))
            elif 0 <= lc < 100 and arr[lr][lc] == 1:
                Q.append((lr, lc))
    # for ar in arr:
    #     print(ar)
    print(f'#{TC}', result)