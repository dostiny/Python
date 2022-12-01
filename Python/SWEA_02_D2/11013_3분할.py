for TC in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 1000000
    for i in range(1, N - 1):
        for j in range(N - 1, i, -1):
            num1 = sum(arr[:i])
            num2 = sum(arr[i:j])
            num3 = sum(arr[j:])
            max_v = max(num1, num2, num3)
            min_v = min(num1, num2, num3)
            if result > max_v - min_v:
                result = max_v - min_v
    print(f'#{TC}' ,result)