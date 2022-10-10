F, S, G, U, D = map(int, input().split())

def bfs(n):
    if n == G:
        return

tpoint = 1
cnt = 0
while True:
    cnt += 1
    if S + U < G:
        S += U
    elif S + U > G:
        S -= D

    if S == G:
        ans = cnt
        break
    elif S < 1 or F < S:
        ans = 'use the stairs'
        break
print(ans)