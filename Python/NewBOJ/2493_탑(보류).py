import sys

input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))

arr = [0 for _ in range(N)]

for i in range(N - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        if tower[i] < tower[j]:
            arr[i] = j + 1
            break

for k in arr:
    print(k, end=' ')