for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input()))
    visited = [0] * N
    max_v, max_i = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i] == arr[j]:
                visited[i] += 1
        if max_i <= visited[i] and max_v < arr[i]:
            max_i = visited[i]
            max_v = arr[i]

    print(f'#{TC}', max_v, max_i)