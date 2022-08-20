import sys
sys.stdin = open('12387_input.txt', 'r')

for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    S = 0
    for i in range(M):  # 첫번째 구간의 합
        S += arr[i]
    max_sum = min_sum = S

    for e in range(M, N):   # 두번째 구간부터 모든 구간의 끝 인덱스
        S = S - arr[e] - arr[e - M]
        if max_sum < S:
            max_sum = S
        if min_sum > S:
            min_sum = S

    print(f'#{T} {max_sum - min_sum}')
