import sys

sys.stdin = open('12385_input.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    # [0] + [1, 3, 5, 7, 9] + [10]
    station = [0] + list(map(int, input().split())) + [N]

    cur = 0 # 현재 위치
    cnt = 0 # 충전횟수
    for i in range(1, M+2):
        # 충전소 사이의 거리를 체크
        if station[i] - station[i-1] > K:   # 갈수 없음
            cnt = 0
            break
        # 충전할 위치를 결정
        if cur + K < station[i]:
            cur = station[i - 1]
            cnt += 1
    print(cnt)
