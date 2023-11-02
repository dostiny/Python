import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    result = 'Impossible'
    s1, s2 = input().split()
    s1 = sorted(list(map(str, s1)))
    s2 = sorted(list(map(str, s2)))
    if s1 == s2:
        result = 'Possible'
    print(result)