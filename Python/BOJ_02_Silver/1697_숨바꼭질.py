from collections import deque

N, K = map(int, input().split())

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(ans[x])
            break
        for j in (x - 1, x + 1, x * 2):
            if 0 <= j <= MAX and not ans[j]:
                ans[j] = ans[x] + 1
                q.append(j)

MAX = 100000
ans = [0] * (MAX + 1)

bfs()