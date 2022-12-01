import sys; sys.stdin = open('input/12398_input.txt', 'r')

def dfs(v):
    visited[v] = 1
    for j in G[v]:
        if visited[j] == 0:
            dfs(j)

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for i in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
    S, E = map(int, input().split())
    dfs(S)
    if visited[E] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')