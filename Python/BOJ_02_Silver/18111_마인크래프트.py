import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
block = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]
ans, idx = 999999999, 0

for i in range(257):
    use, take = 0, 0
    for r in range(N):
        for c in range(M):
            if block[r][c] > i:
                take += block[r][c] - i
            else:
                use += i - block[r][c]

    if use <= take + B:
        count = take * 2 + use
        if count <= ans:
            ans = count
            idx = i

print(ans, idx)