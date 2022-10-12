def ans(s, li):
    if len(li) == M:
        print(*li)
    else:
        for i in range(s, N):
            ans(i, li + [arr[i]])


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

ans(0, [])