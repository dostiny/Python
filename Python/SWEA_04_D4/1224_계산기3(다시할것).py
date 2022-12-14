for TC in range(1, 11):
    N = int(input())
    arr = list(input())
    result = []
    kpoint = 0
    for i in range(N):
        if arr[i].isdigit():
            if kpoint == 0:
                result.append(int(arr[i]))
            else:
                pass
        elif arr[i] == '(':
            kpoint = 1
        elif arr[i] == ')':
            kpoint = 0
        elif arr[i] == '+':
            pass
        elif arr[i] == '*':
            pass
