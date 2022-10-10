from collections import deque

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]
# Q = deque(list(map(int, input().strip())) for _ in range(N))
L, P = map(int, input().strip())
print(arr)