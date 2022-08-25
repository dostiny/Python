N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
house = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 'A':
            house += [['A', r, c]]
        elif arr[r][c] == 'B':
            house += [['B', r, c]]
        elif arr[r][c] == 'C':
            house += [['C', r, c]]
# print(house)
dy = [-1, 1, 0, 0]  # 상 하 좌 우
dx = [0, 0, -1, 1]  # 상 하 좌 우
sur = 0
for i in house:
    r, c = i[1], i[2]
    if i[0] == 'A':
        sur = 1
    elif i[0] == 'B':
        sur = 2
    elif i[0] == 'C':
        sur = 3
    for d in range(4):
        for j in range(1, 1+sur):
            nr, nc = r + dy[d] * j, c + dx[d] * j
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 'H':
                    arr[nr][nc] = 'O'
# for ar in arr:
#     print(ar)
cnt = 0
for r in range(N):
    for c in range(N):
        if arr[r][c] == 'H':
            cnt += 1
print(cnt)