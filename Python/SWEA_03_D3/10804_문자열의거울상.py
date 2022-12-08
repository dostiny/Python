for TC in range(1, int(input()) + 1):
    arr = list(input())
    # print(arr)
    result = ''
    n = len(arr)
    for _ in range(n):
        a = arr.pop()
        if a == 'b':
            result += 'd'
        elif a == 'd':
            result += 'b'
        elif a == 'p':
            result += 'q'
        elif a == 'q':
            result += 'p'
    print(f'#{TC}', result)