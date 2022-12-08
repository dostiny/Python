from collections import deque

N, K = map(int, input().split())

Q = deque()
for i in range(N):
    Q.append(i + 1)
cnt, num = 0, N
ans = []
while num != 0:
    cnt += 1
    if cnt == K:
        a = Q.popleft()
        ans.append(str(a))
        cnt = 0
        num -= 1
    else:
        a = Q.popleft()
        Q.append(a)
print(f"<{', '.join(ans)}>")