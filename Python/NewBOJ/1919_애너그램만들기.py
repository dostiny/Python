import sys

input = sys.stdin.readline

li = [0] * 26

for i in list(input().strip()):
    li[ord(i) - 97] += 1
for j in list(input().strip()):
    li[ord(j) - 97] -= 1

print(sum(map(abs, li)))