import sys
input = sys.stdin.readline()
arr = list(input)
arr.pop()
stack = []
result = 0
top = 1

for i in range(len(arr)):

    if arr[i] == "(":
        stack.append(arr[i])
        top *= 2

    elif arr[i] == "[":
        stack.append(arr[i])
        top *= 3

    elif arr[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        if arr[i-1] == "(":
            result += top
        stack.pop()
        top //= 2

    else:
        if not stack or stack[-1] == "(":
            result = 0
            break
        if arr[i-1] == "[":
            result += top

        stack.pop()
        top //= 3

if stack:
    print(0)
else:
    print(result)