import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
numQ = deque(i + 1 for i in range(N))
pickli = list(map(int, input().split()))
cnt = 0

# print(pickQ)

for num in pickli:
    while True:
        if numQ[0] == num:
            numQ.popleft()
            break
        else:
            if numQ.index(num) <= len(numQ) // 2:
                numQ.rotate(-1)
                cnt += 1
            else:
                numQ.rotate(1)
                cnt += 1
print(cnt)


# 1 6 3 2 7 9 8 4 10 5
'''
1234567890  cnt 0
234567890   cnt 0


'''