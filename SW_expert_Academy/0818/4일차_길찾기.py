import sys; sys.stdin = open('input/4일차_input.txt', 'r')

def dfs(v):
    visited[v] = 1
    for j in G[v]:
        if visited[j] == 0:
            dfs(j)

for i in range(10):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[] for _ in range(100)]
    visited = [0] * 100
    for i in range(0, N*2, 2):
        u, v = arr[i], arr[i+1]
        G[u].append(v)
    # print(G)
    dfs(0)
    if visited[99] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

