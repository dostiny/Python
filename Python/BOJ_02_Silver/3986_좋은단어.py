cnt = 0
for _ in range(int(input())):
    top = -1
    s = list(input())
    stack = [0] * len(s)
    for i in s:
        if stack[top] == i:
            stack[top] = 0
            top -= 1
        else:
            top += 1
            stack[top] = i
    if top == -1:
        cnt += 1
print(cnt)