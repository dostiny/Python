for TC in range(1, int(input()) + 1):
    string = list(input())
    arr = [0] * len(string)
    top = -1
    cnt = 0
    for i in string:
        if arr[top] == i:
            arr[top] = 0
            top -= 1
        else:
            top += 1
            arr[top] = i
    print(f'#{TC}', top + 1)