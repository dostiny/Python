import sys

sys.stdin = open('11084_input.txt', 'r')

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
    max_v = ai[0]
    min_v = ai[0]
    max_idx = 0
    min_idx = 0
    for i in range(N):
        if max_v <= ai[i]:
            max_v = ai[i]
            max_idx = i
    for j in range(N):
        if min_v > ai[j]:
            min_v = ai[j]
            min_idx = j
    if max_idx > min_idx:
        result = max_idx - min_idx
    elif min_idx > max_idx:
        result = min_idx - max_idx
    print(f'#{test_case} {result}')