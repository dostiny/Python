import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(input()))
stack = []
result = 0
for i in arr:
    while stack and stack[-1] <= i:
        stack.pop()
    stack.append(i)
    result += len(stack) - 1
print(result)