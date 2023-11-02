import sys

input = sys.stdin.readline

N = int(input())

arr = [0] * 9

for i in str(N):
    n = int(i)
    if n == 6 or n == 9:
        n = 6
    arr[n] += 1

if arr[6] % 2:
    arr[6] = arr[6] // 2 + 1
else:
    arr[6] = arr[6] // 2

print(max(arr))