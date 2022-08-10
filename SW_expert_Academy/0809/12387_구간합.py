import sys

sys.stdin = open('12387_input.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    min_v = 10000000
    max_v = 0
    for i in range(N-M+1):
        ans = 0
        for j in range(M): # 0 1 2
            ans += arr[i+j]
        if min_v > ans:
            min_v = ans
        if max_v < ans:
            max_v = ans
    print(f'#{test_case} {max_v - min_v}')