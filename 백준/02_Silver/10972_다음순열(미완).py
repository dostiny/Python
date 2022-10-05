def dfs():
    if len(pick) == N:
        print(pick)
        a = list(pick)
        ans.append(a)
        return

    for i in range(1, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            pick.append(i)
            dfs()
            visited[i] = 0
            pick.pop()

N = int(input())
arr = list(map(int, input().split()))

visited = [0] * (N + 1)
pick = []
ans = []
dfs()
idx = 0
for i in range(len(ans)):
    if arr == ans[i]:
        idx = i
        if idx == len(ans)-1:
            idx = -1
if idx == -1:
    print(idx)
else:
    print(ans[idx+1])