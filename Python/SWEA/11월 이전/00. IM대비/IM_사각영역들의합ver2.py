for test in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sample = [[0]*N for _ in range(N)]
    sum_v = 0
    for _ in range(M):
        sr, sc, le = map(int, input().split())
        for r in range(le):
            for c in range(le):
                tr, tc = sr + r, sc + c
                if 0 <= tr < N and 0 <= tc < N:
                    if sample[tr][tc] != 1:
                        sample[tr][tc] = 1
                        sum_v += arr[tr][tc]
    print(f'#{test} {sum_v}')