def dfs(v):
    global G, result
    if visited[v] == 0:
        return
    elif visited[v] == G:
        result = 1
    elif visited[v]:
        for i in visited[v]:
            dfs(i)

for TC in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    visited = list([] for _ in range(V + 1))
    for _ in range(E):
        s, e = map(int, input().split())
        visited[s].append(e)
    S, G = map(int, input().split())
    result = 0
    dfs(S)
    print(result)