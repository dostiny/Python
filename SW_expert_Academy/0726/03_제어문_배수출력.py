num = int(input())

for i in range(1, num+1):
    print(f'#{i}')
    NM_input = list(map(int, input().split()))
    N = NM_input[0]
    M = NM_input[1]
    if 1 < N <= M <= 1000:
        for j in range(1, M//N):
            print(N * j, end=' ')
        print(N * (M//N))