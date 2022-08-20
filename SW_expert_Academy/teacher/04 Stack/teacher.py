import sys; sys.stdin = open('graph_input.txt', 'r')

V, E = map(int, input().split())
# 정점 번호는 1번 ~ V번까지 사용
# 정점수 만큼 빈 인접 리스트 생성

#그래프 저장
G = [[] for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    # G[v].append(u)
#정점들의 방문정보 저장
print(G)
visited = [0] * (V+1)

def dfs(v): # v: 방문할 정점 번호
    # 정점을 방문한다.
    visited[v] = 1; print(v, end=' ') #방문할떄마다 출력
    # v의 방문하지 않은 인접 정점을 찾는다.
    for w in G[v]:
        if visited[w] == 0:
            dfs(w)          #함수호출을 하면서 방문정보가 저장되는것. w-v로 바뀌며 다시 함수가 돔

dfs(1) # 시작점 1을 인자로 함수 호출

print('')
for i in range(1,V+1):
    print(i, '-->', G[i])