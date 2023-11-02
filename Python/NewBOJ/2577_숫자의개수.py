import sys

input = sys.stdin.readline

mulN = 1
for i in range(3):
    N = int(input())
    mulN *= N

arr = [0] * 10
S = str(mulN)
for j in S:
    arr[int(j)] += 1

for k in arr:
    print(k)