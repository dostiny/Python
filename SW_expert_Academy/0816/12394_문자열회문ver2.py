import sys; sys.stdin = open('input/12394_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    ans = ''

    for r in range(n):
        for c in range(n - m + 1):
            e = c + m - 1
            for i in range(m // 2):
                if arr[r][c + i] != arr[r][n - 1 - i]:
                    break
            else:
                for k in range(c, e + 1):
                    ans += arr[r][k]

    for c in range(n):
        for r in range(n - m + 1):
            e = r + m - 1
            for i in range(m // 2):
                if arr[r + i][c] != arr[n - 1 - i][c]:
                    break
            else:
                for k in range(r, e + 1):
                    ans += arr[k][c]
    print(f'#{test_case} {ans}')