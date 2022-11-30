def comb(n, r, start):
    if r == 0:
        print(*pick)
        return

    for i in range(start, n - r + 1):
        pick.append(arr[i])
        comb(n, r - 1, i + 1)
        pick.pop()

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    else:
        n = arr.pop(0)
        pick = []
        r = 6
        comb(n, r, 0)
        print()