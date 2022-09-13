for test_case in range(1, int(input())+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    arr[0][0] = 1
    for r in range(N-1):
        for c in range(N-1):
            arr[r + 1][c] += arr[r][c]
            arr[r + 1][c + 1] += arr[r][c]
    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                print(arr[i][j], end=' ')
        print()