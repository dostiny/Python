N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
A, B, C = 1, 2, 3
house = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 'A':
            house += [['A', r, c]]
        elif arr[r][c] == 'B':
            house += [['B', r, c]]
        elif arr[r][c] == 'C':
            house += [['C', r, c]]

dy = [-1, 1, 0, 0]  # 상 하 좌 우
dx = [0, 0, -1, 1]  # 상 하 좌 우
d = 0
ty = r + dy[d]
tx = c + dx[d]

for i in arr:
    if i[0] == 'A':
        r, c = i[1], i[2]
        for q in range(A*4):
            arr[ty][tx] = 0
            d += 1
    elif i[0] == 'B':
        r, c = i[1], i[2]
        for q in range(B):
            arr[ty][tx] = 0
    elif i[0] == 'C':
        r, c = i[1], i[2]
        for q in range(C):
            arr[ty][tx] = 0
for ar in arr:
    print(ar)


# cnt = 0
# for j in range(9):
#     for i in range(9):
#         if arr[j][i] == 'H':
#             cnt += 1
# print(cnt)