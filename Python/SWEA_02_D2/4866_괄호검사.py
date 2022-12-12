for TC in range(1, int(input()) + 1):
    arr = list(input())
    stack = [0] * len(arr)
    top, result = -1, 1
    for i in arr:
        if i == '{' or i == '(':
            top += 1
            stack[top] = i
        elif i == '}':
            if stack[top] == '{':
                stack[top] = 0
                top -= 1
            else:
                result = 0
                break
        elif i == ')':
            if stack[top] == '(':
                stack[top] = 0
                top -= 1
            else:
                result = 0
                break
        else:
            continue
        # print(stack)
    if stack[0] != 0:
        result = 0
    print(f'#{TC}', result)
