def ans(li):
    if len(li) == M:
        print(*li)
    else:
        for i in range(N):
            ans(li + [arr[i]])


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

visited = [0] * N
ans([])