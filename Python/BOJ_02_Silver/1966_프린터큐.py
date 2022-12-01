from collections import deque

N = int(input())

for i in range(N):
    n, m = map(int, input().split())
    Q = deque(list(map(int, input().split())))
    count = 0
    while Q:
        best = max(Q)
        front = Q.popleft()
        m -= 1

        if best == front:
            count += 1
            if m < 0:
                print(count)
                break

        else:
            Q.append(front)
            if m < 0:
                m = len(Q) - 1