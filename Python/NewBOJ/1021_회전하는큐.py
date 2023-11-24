import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
order = list(map(int, input().split()))
cnt = 0
idx = 0

arr = deque(i + 1 for i in range(N))
while idx != M:
    i = arr.index(order[idx])
    half = len(arr) // 2
    if i <= half:   # 앞에서 빼기
        for j in range(i):
            arr.append(arr.popleft())
            cnt += 1
    else:           # 뒤에서 빼기
        for j in range(len(arr) - i):
            arr.appendleft(arr.pop())
            cnt += 1
    arr.popleft()
    idx += 1
print(cnt)