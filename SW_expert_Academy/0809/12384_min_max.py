import sys

sys.stdin = open('12384_input.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    min_v = arr[0]
    for i in arr:
        if max_v < i:
            max_v = i
        if min_v > i:
            min_v = i
    print(f'#{test_case} {max_v - min_v}')

