for tc in range(1, int(input())+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    n = N // 2
    result = 0

    # 중앙
    for c in range(N):
        result += farm[n][c]

    # 상단 삼각형
    for ur in range(n):
        sc = n - ur
        ec = 2 * ur + 1
        for c in range(sc, sc + ec):
            result += farm[ur][c]

    # 하단 삼각형
    for dr in range(n):
        sc = n - dr
        ec = 2 * dr + 1
        for c in range(sc, sc + ec):
            result += farm[N-1-dr][c]
    print(f'#{tc} {result}')