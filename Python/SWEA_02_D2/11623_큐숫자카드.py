from collections import deque
for TC in range(1, int(input()) + 1):
    Q = deque([i for i in range(1, int(input()) + 1)])
    while len(Q) != 1:
        Q.popleft()
        a = Q.popleft()
        Q.append(a)
    print(f'#{TC}', Q[0])