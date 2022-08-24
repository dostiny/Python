import sys; sys.stdin = open('graph_input.txt', 'r')
#=====================================================
# 그래프 인접행렬로 저장
V, E = map(int, input().split())    # 정점수, 간선수
G = [[0] * (V + 1) for _ in range(V + 1)]   # 인접 행렬
visited = [0] * (V + 1)
# 간선수만큼 입력 처리
for _ in range(E):
    u, v = map(int, input().split())
    G[u][v] = G[v][u] = 1

def dfs(v):
    visited[v] = 1; print(v, end=' ')
    for w in range(1, V + 1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w)

dfs(1)

#=====================================================
# 그래프 인접리스트로 저장
V, E = map(int, input().split())    # 정점수, 간선수
G = [[] for _ in range(V + 1)]
visited = [0] * (V + 1)

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

def dfs(v): # v = 방문할 정점 번호
    visited[v] = 1 # v를 방문한다.
    print(v, end=' ')
    # v의 인접 정점을 w를 찾는다.
    for w in G[v]:
        if not visited[w]:
            dfs(w)
dfs(1)




