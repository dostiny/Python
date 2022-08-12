import sys
sys.stdin = open('2817_input.txt', 'r')

T = int(input())
N, K = map(int, input().split())
arr = list(map(int, input().split()))

for test_case in range(1, T+1):
    cnt = 0
    for i in range(N):
        num = 0
        for j in range(i, N):
            num += arr[j]
            if K == num:
                cnt += 1
    print(f'#{test_case} {cnt}')