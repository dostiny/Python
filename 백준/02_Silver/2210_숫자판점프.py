def findload(r, c, st):
    if len(st) == 6:
        S.add(st)
        return
    else:
        if r + 1 < 5:
            findload(r + 1, c, st + arr[r + 1][c])
        if r - 1 >= 0:
            findload(r - 1, c, st + arr[r - 1][c])
        if c + 1 < 5:
            findload(r, c + 1, st + arr[r][c + 1])
        if c - 1 >= 0:
            findload(r, c - 1, st + arr[r][c - 1])


arr = [list(map(str, input().split())) for _ in range(5)]
S = set()
for r in range(5):
    for c in range(5):
        findload(r, c, arr[r][c])
ans = len(S)
print(ans)