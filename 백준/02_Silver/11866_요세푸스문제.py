from collections import deque

N, K = map(int, input().split())

queue = deque()
for i in range(N):
    queue.append(i + 1)
cnt, num = 0, N
ans = []
while num != 0:
    cnt += 1
    if cnt == K:
        a = queue.popleft()
        ans.append(str(a))
        cnt = 0
        num -= 1
    else:
        a = queue.popleft()
        queue.append(a)
print(f"<{', '.join(ans)}>")