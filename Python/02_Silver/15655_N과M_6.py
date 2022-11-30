def ans(s, li):
    if len(li) == M:
        print(*li)
    else:
        for i in range(s, N):
            if visited[i] == 0:
                visited[i] = 1
                ans(i + 1, li + [arr[i]])
                visited[i] = 0


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

visited = [0] * N
ans(0, [])