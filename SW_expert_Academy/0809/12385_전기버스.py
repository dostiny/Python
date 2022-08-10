import sys

sys.stdin = open('12386_input.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    bus = K
    for i in range(1, M):
        if arr[i] <= bus:
            cnt += 1
        else:
            cnt = 0
            break
        bus += K
    print(cnt)
