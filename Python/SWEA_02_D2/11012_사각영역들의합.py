for TC in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0
    for _ in range(M):
        r, c, n = map(int, input().split())
        for nr in range(r, r + n):
            for nc in range(c, c + n):
                if nr < N and nc < N and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    result += arr[nr][nc]
    print(f'#{TC}',result)