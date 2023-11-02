import sys

input = sys.stdin.readline

S = input().strip()

alpha = 'abcdefghijklmnopqrstuvwxyz'
aldic = {}

for i in range(len(alpha)):
    aldic[alpha[i]] = i

arr = [0] * 26

for i in S:
    arr[aldic[i]] += 1

for j in arr:
    print(j, end=' ')