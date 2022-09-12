for _ in range(int(input())):
    k = int(input())
    n = int(input())
    arr = [[0] * n for _ in range(k+1)]
    for i in range(n):
        arr[0][i] = i + 1
    for r in range(1, k+1):
        for c in range(n):
            if c == 0:
                arr[r][c] = 1
            else:
                arr[r][c] = arr[r-1][c] + arr[r][c-1]
    print(arr[k][n-1])