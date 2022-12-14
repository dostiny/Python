def back(i, s):
    global result
    if i == N:
        if s < result:
            result = s
        return
    elif s >= result:
        return
    for k in range(N):
        if visited[k] == 0:
            visited[k] = 1
            back(i + 1, s + arr[i][k])
            visited[k] = 0

for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    index = []
    result = 99999999
    back(0, 0)
    print(f'#{TC}', result)