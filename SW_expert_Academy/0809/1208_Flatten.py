import sys

sys.stdin = open('input/1208_input.txt', 'r')

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_idx = 0
    min_idx = 0

    for i in range(N+1):
        max_v = 0
        min_v = 99999
        for j in range(len(arr)):
            if max_v < arr[j]:
                max_v = arr[j]
                max_idx = j
            if min_v > arr[j]:
                min_v = arr[j]
                min_idx = j
        arr[max_idx], arr[min_idx] = max_v-1, min_v+1
    print(f'#{test_case} {max_v-min_v}')