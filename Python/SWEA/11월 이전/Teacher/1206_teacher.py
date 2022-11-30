import sys

sys.stdin = open('input/1206_view_input.txt', 'r')

# T = int(input())
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))   # 1차원 배열을 입력받는 방법
    ans = 0
    for i in range(2, N-3 +1):
        # i 가 기준
        max_val = arr[i - 2]
        if max_val < arr[i - 1]:
            max_val = arr[i - 1]
        if max_val < arr[i + 1]:
            max_val = arr[i + 1]
        if max_val < arr[i + 2]:
            max_val = arr[i + 2]
        # ---------------------------------------------------------
        max_val = arr[i - 2]
        for val in [arr[i-1], arr[i+1], arr[i+2]]:
            if max_val < val:
                max_val = val
        # ---------------------------------------------------------
        if arr[i] > max_val:
            ans += arr[i] - max_val
    print(f'{test_case} {ans}')
