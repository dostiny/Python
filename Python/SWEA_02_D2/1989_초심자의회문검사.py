for TC in range(1, int(input()) + 1):
    arr = list(input())
    n = len(arr) // 2
    result = 0
    for i in range(n):
        if arr[i] != arr[-(i+1)]:
            result = 0
            break
        else:
            result = 1
    print(f'#{TC}', result)