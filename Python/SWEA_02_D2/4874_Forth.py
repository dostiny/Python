for TC in range(1, int(input()) + 1):
    arr = list(input().split())
    result, stack = 0, []
    for i in range(len(arr)):
        if arr[i].isdigit():
            stack.append(int(arr[i]))
        else:
            if len(stack) == 1:
                if arr[i] == '.':
                    result = stack[0]
                else:
                    result = 'error'
                    break
            elif len(stack) > 1:
                if arr[i] == '+':
                    a, b = stack.pop(), stack.pop()
                    stack.append(a + b)
                elif arr[i] == '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(a - b)
                elif arr[i] == '*':
                    a, b = stack.pop(), stack.pop()
                    stack.append(a * b)
                elif arr[i] == '/':
                    a, b = stack.pop(), stack.pop()
                    stack.append(a // b)
            else:
                result = 'error'
                break
        # print(stack)
    print(f'#{TC}', result)