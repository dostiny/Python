N = int(input())
arr = list(map(int, input().split()))
stack = []
answer = [0] * N

for i in range(N):
    while stack:
        if stack[-1][1] > arr[i]:
            answer[i] = stack[-1][0]
            break
        else:
            stack.pop()
    stack.append([i + 1, arr[i]])
print(*answer)