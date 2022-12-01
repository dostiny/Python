import sys
sys.stdin = open('input/12392_input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        k = len(arr) - i
        for j in range(1, k):
            if arr[j - 1] >= arr[j]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
    result = []

    for k in range(5):
        result += [arr[-(1+k)], arr[k]]

    print(f'#{test_case}', end=' ')
    print(*result)