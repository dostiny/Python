import sys

sys.stdin = open('input/12383_gravity_input.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = 0
    max_idx = 0
    for i in range(N):
        if max_v <= arr[i]:
            max_v = arr[i]
            max_idx = i
    for j in range(N):
        if max_v == arr[j]:
            if max_idx < j:
                max_idx = j - max_idx
            elif max_idx > j:
                max_idx = max_idx - j
        else:
            if N - max_idx > max_idx:
                max_idx = N - max_idx
            else:
                max_idx

    print(f'#{test_case} {max_idx}')
