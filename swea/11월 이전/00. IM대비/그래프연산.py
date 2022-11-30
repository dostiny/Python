import sys; sys.stdin = open('input_그래프연산.txt')
from collections import deque

for TC in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    queue = deque()
    visited[N] = 1
    queue.append((N, 0))
    while queue:
        num, cnt = queue.popleft()
        if num == M:
            break
        else:
            arr = [num + 1, num - 1, num * 2, num - 10]
            for i in arr:
                if 0 <= i < 1000001 and visited[i] == 0:
                    queue.append((i, cnt + 1))
                    visited[i] = 1
    print(f'#{TC} {cnt}')