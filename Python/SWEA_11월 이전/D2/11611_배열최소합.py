import sys; sys.stdin = open('input/미로_input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cols = [i for i in range(N)]
    def perm(k):
        if k == N:
            S = 0
            for i in range(N):
                S += arr[i][cols[i]]
            print(cols, S)
            global ans
            if ans > S:
                ans = S
        else:
            for i in range(k, N):
                cols[k], cols[i] = cols[i], cols[k]
                perm(k + 1)
                cols[k], cols[i] = cols[i], cols[k]
    ans = 0xffffffffff
    perm(0)