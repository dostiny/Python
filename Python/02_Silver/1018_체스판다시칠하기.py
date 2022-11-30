N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
ans = []

for r in range(N - 7):
    for c in range(M - 7):
        case1 = case2 = 0
        for j in range(r, r + 8):
            for i in range(c, c + 8):
                if (i + j) % 2 == 0:
                    if arr[j][i] != 'W':
                        case1 += 1
                    if arr[j][i] != 'B':
                        case2 += 1

                else:
                    if arr[j][i] != 'B':
                        case1 += 1
                    if arr[j][i] != 'W':
                        case2 += 1
        ans.append(min(case1, case2))

print(min(ans))