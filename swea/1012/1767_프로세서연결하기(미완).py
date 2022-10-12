def core(n, d):
    global cnt
    if n == C:
        return
    else:
        for i in range(C):
            r, c = i
            for j in range(1, N):
                nr, nc = r + dy[d] * j, c + dx[d] * j
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
                    arr[nr][nc] = 2
                elif arr[nr][nc] != 0:
                    return
                elif 1:
                    pass

for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    corepoint = []
    ans = 0
    for r in range(1, N-1):
        for c in range(1, N - 1):
            if arr[r][c] == 1:
                corepoint.append((r, c))
    C = len(corepoint)
    core(0, 0)