for TC in range(1, int(input()) + 1):
    N = int(input())
    inputli = list(map(int, input().split()))
    stack = [0] * N
    top = -1
    for i in inputli:
        if i == 0:
            stack[top] = 0
            top -= 1
        else:
            top += 1
            stack[top] = i
    print(f'#{TC}', sum(stack))