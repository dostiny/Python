for TC in range(1, 11):
    N = int(input())
    arr = list(input())
    stack = []
    num = 0
    for i in range(N):
        if arr[i].isdigit():
            n = int(arr[i])
            if num == 0:
                stack.append(n)
            else:
                stack.append(num * n)
                num = 0
        else:
            if arr[i] == '+':
                pass
            elif arr[i] == '*':
                num = int(stack.pop())
        # print(stack)
    print(f'#{TC}', sum(stack))