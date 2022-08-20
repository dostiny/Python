# 사각영역의 표현
N = 10
arr = [[0] * N for _ in range(N)]

# 1) 두 좌표로 사각영역을 표현
#    - 좌상단 꼭지점(r1, c1), 우 하단 꼭지점(r2, c2)
# 사각 영역의 순회

# for r in range(r1, r2 + 1):
#     for c in range(c1, c2 + 1):
#         arr[r][c]

# 2) 좌상단 꼭지점과(r1, c1) 너비(w)와 높이(h)
#
# for r in range(r1, r1 + h):
#     for c in range(c1, c1 + w):

# =======================================

# arr = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]

# N = 3
# for i in range(N):
#     for j in range(N):
#         if i > j:
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

# for line in arr:
#     print(*line)