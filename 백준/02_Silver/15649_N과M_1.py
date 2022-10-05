# ================================================
# ver1
def dfs():
    if len(s) == m:
        print(*s)
        return

    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

n, m = list(map(int, input().split()))
s = []
dfs()

# ================================================
# ver2
def dfs():
    if len(pick) == M:
        print(*pick)
        return

    for i in range(1, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            pick.append(i)
            dfs()
            visited[i] = 0
            pick.pop()


N, M = map(int, input().split())
visited = [0] * (N + 1)
pick = []

dfs()