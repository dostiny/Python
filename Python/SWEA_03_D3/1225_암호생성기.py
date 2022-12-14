from collections import deque
for _ in range(1, 11):
    TC = int(input())
    Q = deque(list(map(int, input().split())))
    while True:
        num = Q.popleft()
        if num // 10: