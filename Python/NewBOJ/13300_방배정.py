import sys

input = sys.stdin.readline

result = 0
N, K = map(int, input().split())
student = [{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}]

for _ in range(N):
    S, Y = map(int, input().split())
    student[S][Y] += 1

for dic in student:
    for i in dic.values():
        result += i // K
        if i % K:
            result += 1

print(result)