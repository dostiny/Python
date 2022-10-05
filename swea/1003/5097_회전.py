from collections import deque

for TC in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    Q = deque(list(map(int, input().split())))
    while M:
        a = Q.popleft()
        Q.append(a)
        M -= 1
    print(f'#{TC}', Q.popleft())