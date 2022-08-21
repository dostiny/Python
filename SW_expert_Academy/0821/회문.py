import sys; sys.stdin = open('input/회문_input.txt', 'r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    ans = ''
    # 가로 확인
    for r in range(n):
        for c in range(n - m + 1):
            e = c + m - 1
            for i in range(m // 2):
                if arr[r][c + i] != arr[r][n - 1 - i]:
                    break
            else:
                for k in range(c, e + 1):
                    ans += arr[r][k]
    # 세로 확인
    for c in range(n):
        for r in range(n - m + 1):
            e = r + m - 1
            for i in range(m // 2):
                if arr[r + i][c] != arr[n - 1 - i][c]:
                    break
            else:
                for k in range(r, e + 1):
                    ans += arr[k][c]
    print(f'#{tc} {ans}')