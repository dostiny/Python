for TC in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(2, N - 2):
        bild = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        if arr[i] > bild:
            result += arr[i] - bild
    print(f'#{TC}', result)